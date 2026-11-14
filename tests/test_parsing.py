from datetime import date

from lunch.models import DayMenu
from lunch.parsing import clean_dish, find_week, price_of, split_by_weekday, weekday_of
from lunch.scraper import Scraper

TODAY = date(2026, 11, 14)


def test_weekday_of_handles_every_style():
    assert weekday_of("PONDĚLÍ:") == 0
    assert weekday_of("Pondělí, 9. listopadu 2026") == 0
    assert weekday_of("Středa ") == 2
    assert weekday_of("ČTVRTEK:") == 3
    assert weekday_of("PÁTEK") == 4
    assert weekday_of("Polévka: Gulášová") is None


def test_split_by_weekday():
    days = split_by_weekday(["Menu", "Pondělí", "Soup A", "Úterý", "Soup B", "Main B"])
    assert days == {0: ["Pondělí", "Soup A"], 1: ["Úterý", "Soup B", "Main B"]}


def test_price_of():
    assert price_of("| 149,- Kč") == 149
    assert price_of("Segedinský guláš……..…159,-") == 159
    assert price_of("169 Kč") == 169
    assert price_of("39,Kč") == 39
    assert price_of("Denní menu cena : 169Kč") == 169
    assert price_of("(A 1,3,7)") is None
    assert price_of("Vývar s nudlemi (A 1,3)") is None


def test_clean_dish():
    assert clean_dish("I. Segedinský guláš, houskový knedlík*(1a,3,7)….……...……159,-") == "Segedinský guláš, houskový knedlík"
    assert clean_dish("1) Pikantní kuřecí nudličky , jasmínová rýže (A 1)") == "Pikantní kuřecí nudličky, jasmínová rýže"
    assert clean_dish("Francouzská cibulačka*(1a,3,7,9)") == "Francouzská cibulačka"
    assert clean_dish("Gulášová ( A 1,3,7 )") == "Gulášová"


def test_find_week_in_every_format():
    assert find_week("Menu 16.-20.11.2026", TODAY) == date(2026, 11, 16)
    assert find_week("Týdenní menu: od 9.11.- 13.11.2026", TODAY) == date(2026, 11, 9)
    assert find_week("Obědové menu 16-20.11.", TODAY) == date(2026, 11, 16)
    assert find_week("POLEDNÍ MENU V TÝDNU OD 16.11. DO 20.11.2026", TODAY) == date(2026, 11, 16)
    assert find_week("Pondělí, 9. listopadu 2026", TODAY) == date(2026, 11, 9)
    assert find_week("no dates here", TODAY) is None
    # new year: a menu for 29.12.-2.1. seen on 30 December
    assert find_week("Menu 29.12.-2.1.", date(2026, 12, 30)) == date(2026, 12, 28)


def test_subclasses_register_themselves():
    class Demo(Scraper, id="demo-test"):
        name = "Demo"

        def parse(self, text, today):
            return [DayMenu(day=today)]

    assert Scraper.registry["demo-test"] is Demo
    m = Demo().scrape(TODAY, raw=b"<html><body>hi</body></html>")
    assert m.error is None and m.days[0].day == TODAY
    del Scraper.registry["demo-test"]


def test_a_broken_parser_becomes_an_error_not_a_crash():
    class Broken(Scraper, id="broken-test"):
        def parse(self, text, today):
            raise ValueError("layout changed")

    m = Broken().scrape(TODAY, raw=b"<html></html>")
    assert m.days == [] and "layout changed" in m.error
    del Scraper.registry["broken-test"]
