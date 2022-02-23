import requests
from bs4 import BeautifulSoup as bs4
from abc import ABC, abstractmethod


class Scraper(ABC):
    """A website scraping object"""

    def __init__(self, name, url, html_section):
        self.name = name
        self.url = url
        self.html_section = html_section
        self.soup_object = self.soup_object()

    def soup_object(self):
        """

        :return:
        """
        soup = None
        try:
            page = requests.get(self.url)
            content = page.content
            soup = bs4(content, 'html.parser')
        except Exception as e:
            print(f"Soup: Error, {e}", end=' ')
            exit(1)
        return soup

    def daily_menu_from_soup_object(self):
        """

        :return:
        """
        html_tag, html_attr_selector = self.html_section
        desired_part = self.soup_object.find_all(html_tag, attrs=html_attr_selector, recursive=True)
        return desired_part

    @abstractmethod
    def cleanup(self, daily_menu):
        pass


class PdfScraper:
    """A PDF Scraper Object"""
    def __init__(self, name, url):
        self.name = name
        self.url = url
