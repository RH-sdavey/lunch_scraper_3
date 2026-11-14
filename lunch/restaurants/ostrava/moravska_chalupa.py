from datetime import date, timedelta

from ...models import DayMenu, Dish
from ...parsing import clean_dish, find_week, fold, lines_of, price_of, split_by_weekday
from ...scraper import Scraper


class MoravskaChalupa(Scraper, id="moravska-chalupa"):
    name = "Moravská chalupa"
    city, area = "Ostrava", "Organica"
    url = "https://www.moravskachalupa.cz/denni-menu"
    markers = ("Týdenní menu", "Pondělí", "Pátek")

    def parse(self, text: str, today: date) -> list[DayMenu]:
        lines = lines_of(text)
        week = find_week(" ".join(lines[:3]), today)
        menu_price = next((price_of(l) for l in lines if "menu cena" in fold(l)), None)
        out = []
        for wd, day_lines in sorted(split_by_weekday(lines).items()):
            day = DayMenu(day=week + timedelta(days=wd))
            section = None
            for l in day_lines[1:]:
                f = fold(l)
                if f.startswith("polevka"):
                    section = "soup"
                elif f.startswith("hlavni jidlo"):
                    section = "main"
                elif f.startswith("business menu"):
                    section = "business"
                elif "menu cena" in f or "varime pouze" in f:
                    continue
                elif section == "soup":
                    day.dishes.append(Dish(clean_dish(l), "soup"))
                elif section == "main":
                    day.dishes.append(Dish(clean_dish(l), "main", menu_price))
                elif section == "business":
                    day.dishes.append(Dish("Business: " + clean_dish(l), "main", price_of(l)))
            out.append(day)
        return out
