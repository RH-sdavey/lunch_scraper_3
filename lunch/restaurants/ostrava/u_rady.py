import re
from datetime import date, timedelta

from ...models import DayMenu, Dish
from ...parsing import clean_dish, find_week, fold, lines_of, price_of, split_by_weekday
from ...scraper import PdfScraper


class URady(PdfScraper, id="u-rady"):
    name = "Restaurace U Rady"
    city, area = "Ostrava", "Organica · centre"
    url = "https://restauraceurady.cz/tydenni-menu/"     # the page that links this week's PDF

    def parse(self, text: str, today: date) -> list[DayMenu]:
        lines = lines_of(text)
        week = find_week(lines[0], today)
        out = []
        for wd, day_lines in sorted(split_by_weekday(lines).items()):
            day = DayMenu(day=week + timedelta(days=wd))
            body = day_lines[1:]
            for i, l in enumerate(body):
                f = fold(l)
                if f.startswith(("po domluve", "coca cola", "salatek", "seznam alergenu")):
                    break
                if "svatek" in f:
                    day.note = " – ".join(body[i:i + 2])
                    break
                if re.match(r"^[IVX]+\.", l):
                    day.dishes.append(Dish(clean_dish(l), "main", price_of(l)))
                elif not day.dishes:
                    day.dishes.append(Dish(clean_dish(l), "soup"))
            out.append(day)
        return out
