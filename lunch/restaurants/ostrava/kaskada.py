from datetime import date, timedelta

from bs4 import BeautifulSoup

from ...models import DayMenu, Dish
from ...parsing import clean_dish, find_week, fold, lines_of, price_of, split_by_weekday
from ...scraper import Scraper


class Kaskada(Scraper, id="kaskada"):
    name = "Kaskáda"
    city, area = "Ostrava", "Organica · Nová Karolina"
    url = "https://kaskadarestaurant.cz/"

    def block_text(self, raw: bytes) -> str:
        """The page keeps old weeks hidden in the HTML: pick the newest 'Obědové menu' block."""
        soup = BeautifulSoup(raw, "lxml")
        for t in soup(["script", "style"]):
            t.decompose()
        blocks = []
        for el in soup.find_all(string=lambda s: s and "Obědové menu" in s):
            node = el.parent
            while node is not None and "Pátek" not in node.get_text(" "):
                node = node.parent
            if node is not None:
                text = node.get_text("\n")
                week = find_week(text[:80], date.today())
                blocks.append((week or date.min, text))
        if not blocks:
            raise LookupError("no 'Obědové menu' block on the page")
        return max(blocks, key=lambda b: b[0])[1]

    def parse(self, text: str, today: date) -> list[DayMenu]:
        lines = lines_of(text)
        start = next(i for i, l in enumerate(lines) if "Obědové menu" in l)
        lines = lines[start:]
        week = find_week(lines[0], today)
        out = []
        for wd, day_lines in sorted(split_by_weekday(lines).items()):
            if wd > 4:
                continue
            day = DayMenu(day=week + timedelta(days=wd))
            body = day_lines[1:]
            i = 0
            while i < len(body):
                l, f = body[i], fold(body[i])
                if f.startswith("dobrou chut"):
                    break
                if "svatek" in f or "jidelniho listku" in f:
                    day.note = " ".join(x for x in body[i:i + 2] if "svátek" in x.lower() or "lístku" in x.lower()).strip()
                    break
                if f.startswith("polevka"):
                    name = clean_dish(l.split(":", 1)[1] if ":" in l else l)
                    p = price_of(l) or (price_of(body[i + 1]) if i + 1 < len(body) else None)
                    day.dishes.append(Dish(name, "soup", p))
                    i += 2 if price_of(l) is None else 1
                    continue
                if l.rstrip(".").isdigit() and i + 1 < len(body):
                    name = clean_dish(body[i + 1])
                    p = price_of(body[i + 1]) or (price_of(body[i + 2]) if i + 2 < len(body) else None)
                    day.dishes.append(Dish(name, "main", p))
                    i += 3
                    continue
                if f.startswith("k menu 3") and day.dishes:
                    day.dishes[-1].name += " · " + l.split(":", 1)[1].strip()
                i += 1
            out.append(day)
        return out
