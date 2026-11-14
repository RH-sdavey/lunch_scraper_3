"""Every parser against a saved copy of its restaurant's page (tests/fixtures, saved 14 Nov 2026).
When a restaurant redesigns its site, save a new fixture and these show exactly what broke."""
from datetime import date
from pathlib import Path

from lunch.restaurants import load_all
from lunch.scraper import Scraper

load_all()
FIX = Path(__file__).parent / "fixtures"
TODAY = date(2026, 11, 14)


def menu(rid, fixture):
    m = Scraper.registry[rid]().scrape(TODAY, raw=(FIX / fixture).read_bytes())
    assert m.error is None, m.error
    return m


def test_all_four_registered():
    assert {"moravska-chalupa", "kaskada", "paleta", "u-rady"} <= set(Scraper.registry)


def test_moravska_chalupa():
    m = menu("moravska-chalupa", "moravska_chalupa.html")
    assert [d.day for d in m.days] == [date(2026, 11, d) for d in (9, 10, 11, 12, 13)]
    mon = m.days[0].dishes
    assert (mon[0].kind, mon[0].name) == ("soup", "Vývar s nudlemi")
    assert mon[1].name == "Pikantní kuřecí nudličky, jasmínová rýže" and mon[1].price == 169
    assert mon[3].name.startswith("Business: Pečený králík") and mon[3].price == 299
    wed = [d.name for d in m.days[2].dishes]
    assert wed == ["Kulajda", "Vepřové rizoto se sýrem"]           # "we cook only one menu" is not a dish


def test_kaskada_picks_the_newest_week_not_the_hidden_old_ones():
    m = menu("kaskada", "kaskada.html")
    assert m.days[0].day == date(2026, 11, 16)
    mon = m.days[0].dishes
    assert mon[0].kind == "soup" and mon[0].name.startswith("Papriková zelná") and mon[0].price == 39
    assert [d.price for d in mon[1:]] == [149, 169, 279]
    assert mon[3].name.startswith("Steak z vepřové panenské")
    tue = m.days[1]
    assert tue.day == date(2026, 11, 17) and tue.dishes == [] and "svátek" in tue.note.lower()


def test_paleta():
    m = menu("paleta", "paleta.html")
    assert m.days[0].day == date(2026, 11, 9)
    mon = m.days[0].dishes
    assert mon[0].name.startswith("Smažené krůtí řízečky") and mon[0].price == 169
    assert len(mon) == 4 and all(d.kind == "main" for d in mon)
    assert m.days[1].dishes[2].price == 184                         # Hovězí španělský ptáček


def test_u_rady_pdf():
    m = menu("u-rady", "u_rady_menu.pdf")
    assert [d.day for d in m.days] == [date(2026, 11, d) for d in (16, 17, 18, 19, 20)]
    mon = m.days[0].dishes
    assert (mon[0].kind, mon[0].name) == ("soup", "Francouzská cibulačka")
    assert [(d.name, d.price) for d in mon[1:]] == [
        ("Segedinský guláš, houskový knedlík", 159),
        ("Smažená kuřecí játra, bramborová kaše, ledový salát se špekem", 169),
        ("Hovězí steak, omáčka z pečených paprik, hranolky", 219)]
    assert m.days[1].dishes == [] and "Státní svátek" in m.days[1].note


def test_u_stura_menu_picture():
    m = Scraper.registry["u-stura"]().scrape(TODAY, raw=(FIX / "u_stura.html").read_bytes())
    assert m.error is None
    assert m.image == "https://cdn1.artcltn.com/storage/37586/01a1844c-67d8-70e8-bff3-12f4ec51e378/listopad2.png"
