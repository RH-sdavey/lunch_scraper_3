import os
import tempfile
from datetime import date, datetime
from pathlib import Path

os.environ["DATA_DIR"] = tempfile.mkdtemp()
os.environ["LUNCH_NO_SCHEDULER"] = "1"

from fastapi.testclient import TestClient  # noqa: E402

from lunch import main, store  # noqa: E402
from lunch.scraper import Scraper  # noqa: E402

FIX = Path(__file__).parent / "fixtures"
FIXTURES = {"moravska-chalupa": "moravska_chalupa.html", "kaskada": "kaskada.html",
            "paleta": "paleta.html", "u-rady": "u_rady_menu.pdf", "u-stura": "u_stura.html"}


def fill_cache(monkeypatch):
    """Point every scraper at its saved page instead of the internet."""
    for rid, fx in FIXTURES.items():
        monkeypatch.setattr(Scraper.registry[rid], "fetch", lambda self, fx=fx: (FIX / fx).read_bytes())
    monkeypatch.setattr(store, "PAUSE_BETWEEN_S", 0)
    store.refresh_all(date(2026, 11, 14))


def test_lunch_day_rules():
    assert main.lunch_day(datetime(2026, 11, 16, 9)) == date(2026, 11, 16)      # Monday morning: today
    assert main.lunch_day(datetime(2026, 11, 16, 16)) == date(2026, 11, 17)     # after 15:00: tomorrow
    assert main.lunch_day(datetime(2026, 11, 14, 10)) == date(2026, 11, 16)     # Saturday: Monday
    assert main.lunch_day(datetime(2026, 11, 20, 16)) == date(2026, 11, 23)     # Friday evening: Monday


def test_pages_and_api(monkeypatch):
    fill_cache(monkeypatch)
    c = TestClient(main.app)
    page = c.get("/?day=2026-11-16").text
    assert "Kaskáda" in page and "Segedinský guláš" in page and "Státní svátek" not in page
    assert "This week's menu isn't up yet" in page                   # Paleta and Chalupa only have last week
    tue = c.get("/?day=2026-11-17").text
    assert "Státní svátek" in tue
    api = c.get("/api/menus?day=2026-11-16").json()
    first = api["restaurants"][0]
    assert first["dishes"] and api["day"] == "2026-11-16"
    names = {r["name"] for r in api["restaurants"] if r["dishes"]}
    assert names == {"Kaskáda", "Restaurace U Rady"}


def test_refresh_returns_one_card(monkeypatch):
    fill_cache(monkeypatch)
    r = TestClient(main.app).post("/restaurants/paleta/refresh?day=2026-11-09")
    assert r.status_code == 200 and 'id="card-paleta"' in r.text and "Smažené krůtí řízečky" in r.text
    assert TestClient(main.app).post("/restaurants/nope/refresh?day=2026-11-09").status_code == 404


def test_failed_scrape_keeps_the_last_good_menu(monkeypatch):
    fill_cache(monkeypatch)
    monkeypatch.setattr(Scraper.registry["paleta"], "fetch", lambda self: (_ for _ in ()).throw(ConnectionError("down")))
    entry = store.refresh("paleta", force=True)
    assert entry["menu"].days and "down" in entry["menu"].error


def test_status_contract(monkeypatch):
    fill_cache(monkeypatch)
    d = TestClient(main.app).get("/status").json()
    assert isinstance(d["ok"], bool) and len(d["facts"]) == 3


def test_embedded_widget_card(monkeypatch):
    fill_cache(monkeypatch)
    page = TestClient(main.app).get("/?day=2026-11-16").text
    assert "Obecní dům Kobeřice" in page and 'src="https://www.menicka.cz/api/iframe/?id=6942' in page
    api = TestClient(main.app).get("/api/menus?day=2026-11-16").json()
    kob = next(r for r in api["restaurants"] if r["id"] == "obecni-dum-koberice")
    assert kob["embed_url"].startswith("https://www.menicka.cz/api/iframe/")


def test_picture_menu_card(monkeypatch):
    fill_cache(monkeypatch)
    page = TestClient(main.app).get("/?day=2026-11-16").text
    assert "Restaurace U Šťura" in page and "listopad2.png" in page and 'class="menu-img"' in page
