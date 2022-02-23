from time import sleep

import wget
import os

from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Drapal(PdfScraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        self.olo_drapal = './static/assets/pdfs_sites/Drapal.pdf'

        super().__init__(self.data.name, self.data.url)

    def scrape_data(self):
        if os.path.exists(self.olo_drapal):
            os.remove(self.olo_drapal)
        wget.download(self.data.url, self.olo_drapal)
        sleep(2)
        return '<embed src="/static/assets/pdfs_sites/Drapal.pdf" width="1212px" height="1200px" />'
