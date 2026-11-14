import re
from datetime import date

from ...models import DayMenu, Dish
from ...parsing import MONTHS, clean_dish, lines_of, price_of, weekday_of
from ...scraper import Scraper


class Paleta(Scraper, id="paleta"):
    name = "Paleta"
    city, area = "Ostrava", "Organica"
    url = "https://www.paletarestaurant.cz/menu/menu.php"
    website = "https://www.paletarestaurant.cz/"

    # Every day heading carries its full date: "Pondělí, 9. listopadu 2026"
    DAY = re.compile(r"^\w+,\s*(\d{1,2})\.\s*(" + "|".join(MONTHS) + r")\s*(\d{4})", re.I)

    def parse(self, text: str, today: date) -> list[DayMenu]:
        out, day, pending = [], None, None
        for l in lines_of(text):
            m = self.DAY.match(l)
            if m and weekday_of(l) is not None:
                day = DayMenu(day=date(int(m.group(3)), MONTHS[m.group(2).lower()], int(m.group(1))))
                out.append(day)
                pending = None
            elif day is None:
                continue
            elif re.fullmatch(r"\d{2,4}\s*Kč", l) and pending:
                day.dishes.append(Dish(pending, "main", price_of(l)))
                pending = None
            else:
                pending = clean_dish(l)
        return out
