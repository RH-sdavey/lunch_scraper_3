"""The restaurant parser framework (v4 of Sean's lunch scraper design).

    class Paleta(Scraper, id="paleta"):         # registers itself
        name, city, area, url = ...
        markers = ("Tento týden",)               # optional: text that identifies the menu block
        def parse(self, text, today): ...        # this restaurant's own rules -> list[DayMenu]

The base class fetches the page, finds the menu block and hands its text to the subclass.
PdfScraper does the same for restaurants that publish a PDF.
"""
from __future__ import annotations

import io
import re
from abc import ABC, abstractmethod
from datetime import date
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .models import DayMenu, Menu

USER_AGENT = "Mozilla/5.0 (compatible; LunchScraper/4.0; home use; one fetch a few times a day)"


class Scraper(ABC):
    registry: dict[str, type["Scraper"]] = {}

    id: str = ""
    name: str = ""
    city: str = ""
    area: str = ""
    url: str = ""
    website: str = ""          # page people should open (defaults to url)
    markers: tuple[str, ...] = ()

    def __init_subclass__(cls, id: str | None = None, **kw):
        super().__init_subclass__(**kw)
        if id:
            cls.id = id
            Scraper.registry[id] = cls

    # ----- steps (override only what differs) -----

    def fetch(self) -> bytes:
        r = requests.get(self.url, headers={"User-Agent": USER_AGENT}, timeout=20)
        r.raise_for_status()
        return r.content

    def block_text(self, raw: bytes) -> str:
        """Text of the smallest element that contains every marker (or the whole page)."""
        soup = BeautifulSoup(raw, "lxml")
        for t in soup(["script", "style", "noscript"]):
            t.decompose()
        node = soup.body or soup
        if self.markers:
            best = None
            for el in soup.find_all(True):
                txt = el.get_text(" ")
                if all(m.lower() in txt.lower() for m in self.markers):
                    best = el                     # find_all is document order: later = deeper
            node = best or node
        return node.get_text("\n")

    @abstractmethod
    def parse(self, text: str, today: date) -> list[DayMenu]:
        """Each restaurant's own rules: menu text -> days with soups and mains."""

    # ----- the whole job -----

    def scrape(self, today: date, raw: bytes | None = None) -> Menu:
        try:
            raw = raw if raw is not None else self.fetch()
            days = self.parse(self.block_text(raw), today)
            return Menu(restaurant=self.id, days=days)
        except Exception as e:  # noqa: BLE001 - one restaurant failing never stops the others
            return Menu(restaurant=self.id, error=f"{type(e).__name__}: {str(e)[:200]}")

    @classmethod
    def info(cls) -> dict:
        return {"id": cls.id, "name": cls.name, "city": cls.city, "area": cls.area,
                "website": cls.website or cls.url}


class EmbedScraper(Scraper):
    """For restaurants whose menu only exists in a widget they embed on their own site
    (e.g. a Menicka.cz iframe). Nothing is fetched or scraped: the card shows the same
    widget, loaded by the viewer's browser exactly as on the restaurant's page."""

    embed_url: str = ""
    embed_height: int = 560

    def fetch(self) -> bytes:
        return b""

    def block_text(self, raw: bytes) -> str:
        return ""

    def parse(self, text: str, today: date) -> list[DayMenu]:
        return []

    @classmethod
    def info(cls) -> dict:
        return {**super().info(), "embed_url": cls.embed_url, "embed_height": cls.embed_height}


class ImageScraper(Scraper):
    """For restaurants that post the menu as a picture on their own page: find the current
    picture (its address changes with each new menu) and show it in the card."""

    image_pattern = re.compile(r"\.(png|jpe?g|webp)(\?|$)", re.I)
    skip = re.compile(r"logo|icon|favicon|flag|facebook|instagram", re.I)

    def find_image(self, raw: bytes) -> str:
        soup = BeautifulSoup(raw, "lxml")
        for img in soup.find_all("img"):
            src = img.get("src") or img.get("data-src") or ""
            if self.image_pattern.search(src) and not self.skip.search(src):
                src = re.sub(r"\?.*$", "", src)
                return urljoin(self.url, "https:" + src if src.startswith("//") else src)
        raise LookupError("no menu picture on the page")

    def parse(self, text: str, today: date) -> list[DayMenu]:
        return []

    def scrape(self, today: date, raw: bytes | None = None) -> Menu:
        try:
            raw = raw if raw is not None else self.fetch()
            return Menu(restaurant=self.id, image=self.find_image(raw))
        except Exception as e:  # noqa: BLE001
            return Menu(restaurant=self.id, error=f"{type(e).__name__}: {str(e)[:200]}")


class PdfScraper(Scraper):
    """For restaurants that publish the week as a PDF linked from a page."""

    pdf_link = re.compile(r"\.pdf($|\?)", re.I)

    def find_pdf_url(self, page: bytes) -> str:
        soup = BeautifulSoup(page, "lxml")
        for a in soup.find_all("a", href=True):
            if self.pdf_link.search(a["href"]):
                return urljoin(self.url, a["href"])
        raise LookupError("no PDF link on the menu page")

    def fetch(self) -> bytes:
        page = super().fetch()
        r = requests.get(self.find_pdf_url(page), headers={"User-Agent": USER_AGENT}, timeout=30)
        r.raise_for_status()
        return r.content

    def block_text(self, raw: bytes) -> str:
        import pdfplumber
        with pdfplumber.open(io.BytesIO(raw)) as pdf:
            return "\n".join(p.extract_text() or "" for p in pdf.pages)
