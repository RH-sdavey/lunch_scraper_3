"""Lunch Scraper v4: today's lunch menus around Organica (and anywhere else a parser exists)."""
from __future__ import annotations

import asyncio
import os
from contextlib import asynccontextmanager
from datetime import date, datetime, timedelta

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import store
from .restaurants import load_all
from .parsing import week_start
from .scraper import Scraper

load_all()
HERE = os.path.dirname(__file__)
templates = Jinja2Templates(directory=os.path.join(HERE, "templates"))
DAYS_CZ = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
DAYS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def lunch_day(now: datetime | None = None) -> date:
    """The day worth showing: today on weekdays, after 15:00 tomorrow's, at weekends Monday's."""
    now = now or datetime.now()
    d = now.date()
    if now.hour >= 15:
        d += timedelta(days=1)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d


async def scheduler():
    """Refresh at start-up if stale, then every 2 h on weekdays 6:00-14:00, twice a day otherwise."""
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, store.refresh_all)
    while True:
        now = datetime.now()
        busy = now.weekday() < 5 and 6 <= now.hour < 14
        await asyncio.sleep(2 * 3600 if busy else 6 * 3600)
        await loop.run_in_executor(None, store.refresh_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = None if os.environ.get("LUNCH_NO_SCHEDULER") else asyncio.create_task(scheduler())
    yield
    if task:
        task.cancel()


app = FastAPI(title="Lunch Scraper", version="4.0", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=os.path.join(HERE, "static")), name="static")


def cards(day: date) -> list[dict]:
    cache = store.load()
    out = []
    for rid, cls in sorted(Scraper.registry.items(), key=lambda kv: kv[1].name):
        entry = cache.get(rid)
        menu = entry["menu"] if entry else None
        # has_week: the restaurant posted the menu for *this* week (so a missing day means "closed")
        this_week = bool(menu and any(week_start(x.day) == week_start(day) for x in menu.days))
        info = cls.info()
        if menu and menu.image:                       # menu published as a picture
            out.append({**info, "day": None, "has_week": True, "error": menu.error, "image": menu.image,
                        "fetched_at": entry["fetched_at"]})
            continue
        if info.get("embed_url"):                     # widget-only restaurant: always "has a menu"
            out.append({**info, "day": None, "has_week": True, "error": None, "fetched_at": None, "embed": True})
            continue
        out.append({**info, "day": menu.for_day(day) if menu else None,
                    "has_week": this_week, "error": menu.error if menu else None,
                    "fetched_at": entry["fetched_at"] if entry else None})
    # restaurants with food today first
    # restaurants with food today first (embedded widgets count as food), then the rest
    return sorted(out, key=lambda c: (not (c.get("embed") or c.get("image") or (c["day"] and c["day"].dishes)), c["name"]))


def day_label(d: date) -> dict:
    today = date.today()
    rel = "Today" if d == today else "Tomorrow" if d == today + timedelta(days=1) else DAYS_EN[d.weekday()]
    return {"rel": rel, "cz": f"{DAYS_CZ[d.weekday()]} {d.day}. {d.month}.", "iso": d.isoformat()}


@app.get("/", response_class=HTMLResponse)
def index(request: Request, day: str | None = None):
    d = date.fromisoformat(day) if day else lunch_day()
    week = [d - timedelta(days=d.weekday()) + timedelta(days=i) for i in range(5)]
    return templates.TemplateResponse(request, "index.html", {
        "cards": cards(d), "label": day_label(d), "week": [day_label(x) for x in week], "selected": d.isoformat()})


@app.post("/restaurants/{rid}/refresh", response_class=HTMLResponse)
def refresh_one(request: Request, rid: str, day: str):
    if rid not in Scraper.registry:
        raise HTTPException(404)
    store.refresh(rid)
    card = next(c for c in cards(date.fromisoformat(day)) if c["id"] == rid)
    return templates.TemplateResponse(request, "_card.html", {"c": card, "selected": day})


# ---------- JSON API ----------

@app.get("/api/restaurants")
def api_restaurants():
    return [cls.info() for cls in Scraper.registry.values()]


@app.get("/api/menus")
def api_menus(day: str | None = None):
    d = date.fromisoformat(day) if day else lunch_day()
    return {"day": d.isoformat(), "restaurants": [
        {**{k: c[k] for k in ("id", "name", "city", "area", "website", "error", "fetched_at")},
         "note": c["day"].note if c["day"] else None,
         "embed_url": c.get("embed_url"), "image": c.get("image"),
         "dishes": [vars(x) for x in c["day"].dishes] if c["day"] else []} for c in cards(d)]}


# ---------- HomeHub ----------

@app.get("/health")
def health():
    return {"ok": True}


@app.get("/status")
def status():
    d = lunch_day()
    cs = cards(d)
    with_food = sum(1 for c in cs if c["day"] and c["day"].dishes)
    broken = [c["name"] for c in cs if c["error"]]
    times = [c["fetched_at"] for c in cs if c["fetched_at"]]
    return {"ok": not broken, "facts": [
        {"label": f"Menus for {day_label(d)['rel'].lower()}", "value": f"{with_food} of {len(cs)}"},
        {"label": "Last checked", "value": max(times)[11:16] if times else "not yet"},
        {"label": "Parsers needing a look", "value": ", ".join(broken) if broken else "none"},
    ]}
