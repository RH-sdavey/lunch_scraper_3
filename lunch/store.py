"""Cache of the latest menu per restaurant (a small JSON file) and the polite refresh logic."""
from __future__ import annotations

import json
import os
import threading
import time
from datetime import date, datetime

from .models import Menu
from .scraper import Scraper

DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(__file__), "..", "data"))
CACHE = os.path.join(DATA_DIR, "menus.json")
MIN_REFRESH_S = 600            # never hit the same restaurant more than once per 10 minutes
PAUSE_BETWEEN_S = 2            # spread the requests out

_lock = threading.Lock()


def load() -> dict:
    try:
        with open(CACHE, encoding="utf-8") as f:
            raw = json.load(f)
        return {rid: {"menu": Menu.from_dict(v["menu"]), "fetched_at": v["fetched_at"]} for rid, v in raw.items()}
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return {}


def _save(cache: dict):
    os.makedirs(DATA_DIR, exist_ok=True)
    tmp = CACHE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({rid: {"menu": v["menu"].to_dict(), "fetched_at": v["fetched_at"]} for rid, v in cache.items()},
                  f, ensure_ascii=False, indent=1)
    os.replace(tmp, CACHE)


def refresh(rid: str, today: date | None = None, force: bool = False) -> dict:
    """Scrape one restaurant (unless it was fetched in the last 10 minutes) and keep the result.
    A failed scrape keeps the previous good menu and records the error next to it."""
    today = today or date.today()
    with _lock:
        cache = load()
        prev = cache.get(rid)
        if prev and not force and time.time() - datetime.fromisoformat(prev["fetched_at"]).timestamp() < MIN_REFRESH_S:
            return prev
    menu = Scraper.registry[rid]().scrape(today)
    with _lock:
        cache = load()
        if menu.error and cache.get(rid) and cache[rid]["menu"].days:
            kept = cache[rid]["menu"]
            kept.error = menu.error
            menu = kept
        cache[rid] = {"menu": menu, "fetched_at": datetime.now().isoformat(timespec="seconds")}
        _save(cache)
        return cache[rid]


def refresh_all(today: date | None = None):
    for i, rid in enumerate(sorted(Scraper.registry)):
        if i:
            time.sleep(PAUSE_BETWEEN_S)
        refresh(rid, today)
