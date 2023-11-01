import os
from time import sleep

import requests
import wget
from bs4 import BeautifulSoup as Bs4
from abc import ABC, abstractmethod
from data.Data import restaurant_data


class Scraper(ABC):
    """A website daily menu scraping object"""

    def __init__(self, **kwargs):
        self.data = restaurant_data(kwargs.get('city'), kwargs.get('district'), kwargs.get('restaurant'))
        self.today = kwargs.get("today", "No date available")
        self.url = self.data.url
        self.html_section = self.data.html_section
        self.soup = self.soup_object()

    def soup_object(self):
        """Requests a sites contents, and parses the html into a "soup" object -> self.soup

        :return: soup object representing websites html
        :rtype: BeautifulSoup
        :raises Exception if error on scraping/parsing
        """
        try:
            page = requests.get(self.url)
            content = page.content
            soup = Bs4(content, 'html.parser')
        except Exception as e:
            print(f"Soup: Error, {e}", end=' ')
            exit(1)
        return soup

    def daily_menu_from_soup_object(self):
        """Matches all the html tags that are parsed by self.html_section

        :return: the denni menu part of the soup (html) object
        :rtype: ResultSet
        """
        html_tag, html_attr_selector = self.html_section
        desired_part = self.soup.find_all(html_tag, attrs=html_attr_selector, recursive=True)
        return desired_part

    def scrape_data(self):
        return self.cleanup(self.daily_menu_from_soup_object())

    @abstractmethod
    def cleanup(self, daily_menu):
        """Each website has its own html implementation and must be cleaned in their own way"""
        pass


class PdfScraper:
    """A PDF Scraper Object"""
    def __init__(self, **kwargs):
        self.data = restaurant_data(kwargs.get('city'), kwargs.get('district'), kwargs.get('restaurant'))
        self.today = kwargs.get("today", "no date available")
        self.url = ''
        self.local_path = "/static/assets/pdfs_sites/"

    def scrape_data(self, menu_name, custom_url):
        self.url = custom_url
        embed_path = f"{self.local_path}{menu_name}"
        local_path = f".{self.local_path}{menu_name}"
        self.cleanup_old(local_path)
        self.wget_pdf(local_path)
        return f'<embed src="{embed_path}" width="1212px" height="1200px" />'

    def wget_pdf(self, local_path):
        wget.download(self.url, local_path)
        sleep(2)

    @staticmethod
    def cleanup_old(local_path):
        os.remove(local_path) if os.path.exists(local_path) else None


