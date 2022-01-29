import requests
from bs4 import BeautifulSoup as bs4
import unidecode
from abc import ABC, abstractmethod
from collections import namedtuple


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
            data = page.content
            soup = bs4(data, 'html.parser')
        except Exception as e:
            print(f"Soup: Error, {e}", end=' ')
            exit(1)
        return soup

    def daily_menu_from_soup_object(self):
        """

        :return:
        """
        html_tag, html_attr_selector = self.html_section
        desired_part = self.soup_object.find(html_tag, attrs=html_attr_selector)
        print("TODO: next line could be json/list if better?")
        return desired_part

    @abstractmethod
    def cleanup(self, daily_menu):
        pass
