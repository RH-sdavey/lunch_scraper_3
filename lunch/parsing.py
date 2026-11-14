"""Shared helpers for Czech lunch menus: weekdays, dates, prices, allergen clean-up."""
from __future__ import annotations

import re
import unicodedata
from datetime import date, timedelta

WEEKDAYS = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
MONTHS = {"ledna": 1, "února": 2, "března": 3, "dubna": 4, "května": 5, "června": 6, "července": 7,
          "srpna": 8, "září": 9, "října": 10, "listopadu": 11, "prosince": 12}


def fold(s: str) -> str:
    """Lowercase without diacritics: 'Pondělí' -> 'pondeli'."""
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


_FOLDED_DAYS = [fold(d) for d in WEEKDAYS]


def weekday_of(line: str) -> int | None:
    """0-6 if the line starts with a Czech day name ('PONDĚLÍ:', 'Pondělí, 9. listopadu', 'Středa ')."""
    head = fold(line.strip())
    for i, d in enumerate(_FOLDED_DAYS):
        if re.match(rf"{d}\b", head):
            return i
    return None


def lines_of(text: str) -> list[str]:
    return [re.sub(r"\s+", " ", l).strip() for l in text.splitlines() if l.strip()]


def split_by_weekday(lines: list[str]) -> dict[int, list[str]]:
    """{weekday: [lines after that day's heading]}; the heading line itself is kept first."""
    out, current = {}, None
    for l in lines:
        wd = weekday_of(l)
        if wd is not None:
            current = wd
            out[current] = [l]
        elif current is not None:
            out[current].append(l)
    return out


PRICE = re.compile(r"(\d{2,4})\s*(?:,\s*[-–]?\s*(?:Kč|kč)?|Kč|kč|CZK)(?![\d])")


def price_of(s: str) -> int | None:
    m = PRICE.search(s)
    return int(m.group(1)) if m else None


ALLERGENS = re.compile(r"\*?\s*\(\s*(?:A\s*)?[\d\s,a-z]+\)\s*$", re.I)


def clean_dish(s: str) -> str:
    """Drop allergen codes, dotted price leaders, prices, numbering like '1)', 'I.', '2.'."""
    s = re.sub(r"[.…]{3,}.*$", "", s)                     # 'Segedin…………159,-' -> 'Segedin'
    s = PRICE.sub("", s)
    s = re.sub(r"\|\s*$", "", s.strip())
    s = re.sub(r"^\s*(?:[IVX]+\.|\d+[.)])\s*", "", s)    # numbering
    for _ in range(2):
        s = ALLERGENS.sub("", s.strip())
    s = re.sub(r"\s*\*\s*$", "", s)
    s = re.sub(r"\s+([,.])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip(" ,|")


def week_start(d: date) -> date:
    return d - timedelta(days=d.weekday())


def find_week(text: str, today: date) -> date | None:
    """Monday of the week a menu is for, from '16.-20.11.2026', 'od 9.11.- 13.11.2026', '16-20.11.',
    'OD 16.11. DO 20.11.2026' or 'Pondělí, 9. listopadu 2026'. Year defaults to the nearest one to today."""
    def nearest(day, month, year=None):
        if year:
            return date(int(year), month, day)
        cands = [date(today.year + k, month, day) for k in (-1, 0, 1)]
        return min(cands, key=lambda c: abs((c - today).days))

    m = re.search(r"(\d{1,2})\s*\.?\s*(?:(\d{1,2})\s*\.\s*)?\s*[-–]\s*(?:do\s*)?(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})?", text, re.I)
    if not m:
        m2 = re.search(r"od\s*(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(?:\d{4})?\s*do\s*(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})?", text, re.I)
        if m2:
            return week_start(nearest(int(m2.group(1)), int(m2.group(2)), m2.group(5)))
    if m:
        start_day, start_month, _, end_month, year = m.groups()
        return week_start(nearest(int(start_day), int(start_month or end_month), year))
    m = re.search(r"(\d{1,2})\.\s*(" + "|".join(MONTHS) + r")\s*(\d{4})?", text, re.I)
    if m:
        return week_start(nearest(int(m.group(1)), MONTHS[m.group(2).lower()], m.group(3)))
    return None
