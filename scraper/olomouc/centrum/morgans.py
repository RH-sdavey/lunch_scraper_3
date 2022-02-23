from datetime import datetime
from time import sleep

import wget
import os

from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Morgans(PdfScraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        self.olo_morgans = './static/assets/pdfs_sites/olo-morgans.jpg'

        super().__init__(self.data.name, self.data.url)

    def scrape_data(self):
        day = datetime.now().day
        month = datetime.now().month
        full_month = f"0{month}" if month < 10 else month
        year = datetime.now().year
        if os.path.exists(self.olo_morgans):
            os.remove(self.olo_morgans)
            url = self.data.url + f'{year}/{full_month}/{day}.{month}.-web.jpg'
        wget.download(self.data.url + f'{year}/{full_month}/{day}.{month}.-web.jpg', self.olo_morgans)
        sleep(2)
        return '<img src="/static/assets/pdfs_sites/olo-morgans.jpg"  style="width=1rem; height=1rem;" />'

