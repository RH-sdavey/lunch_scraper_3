# Lunch Scraper v4

Today's lunch menus (*denní menu*) from restaurants' own websites, on one page. A FastAPI backend with HTMX pages, run in Docker on the HomeHub (`http://<mac-ip>:8085`).

> v3 (Flask, Brno / Olomouc / Ostrava, 2022-23) is kept as the git tag [`v3`](../../tree/v3).

## How it works
- **`lunch/scraper.py`**: `Scraper(ABC)` fetches a restaurant's page, finds the menu block and hands its text to the subclass's `parse()`. `PdfScraper` does the same for weekly PDFs. Subclasses **register themselves**: `class Paleta(Scraper, id="paleta")`.
- **`lunch/restaurants/<city>/<restaurant>.py`**: one small file per restaurant with its own parsing rules, returning structured `DayMenu` / `Dish` (soup or main, name, price).
- **`lunch/parsing.py`**: shared Czech-menu helpers (weekday names, week dates, prices, allergen clean-up).
- **`lunch/store.py`**: a cache in `data/menus.json`. It refreshes politely (at most once per 10 minutes per restaurant, 2 s between restaurants), and a failed fetch keeps the last good menu.
- Menus are weekly, and restaurants post the new week on different days. The app works out which week each menu is for, so it never shows last week's menu as today's.

## Adding a restaurant
1. Save its page to `tests/fixtures/`.
2. Add `lunch/restaurants/<city>/<name>.py` with a `Scraper` (or `PdfScraper`) subclass and its `parse()`.
3. Add a test in `tests/test_restaurants.py` with a few real dishes and prices from the fixture.

## API
- `GET /api/menus?day=YYYY-MM-DD`: every restaurant's menu for a day (defaults to the next lunch day).
- `GET /api/restaurants`
- `POST /restaurants/{id}/refresh`: check one restaurant again.
- `/status` and `/health`: for HomeHub.

## Restaurants (Ostrava, Organica)
Kaskáda (Nová Karolina), Paleta, Restaurace U Rady (weekly PDF), Moravská chalupa.

## Restaurants (around Štěpánkovice)
Obecní dům Kobeřice: shown with its own embedded Menicka.cz widget (`EmbedScraper`), since that is the only place it publishes dishes.
