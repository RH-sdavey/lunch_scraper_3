from time import sleep

import wget
import os

from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Iqmoravka(PdfScraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        self.brno_iqmoravka = './static/assets/pdfs_sites/MenuIQ.pdf'

        super().__init__(self.data.name, self.data.url)

    def scrape_data(self):
        if os.path.exists(self.brno_iqmoravka):
            os.remove(self.brno_iqmoravka)
        wget.download(self.data.url + self.day_pdf(), self.brno_iqmoravka)
        sleep(2)
        return '<embed src="/static/assets/pdfs_sites/MenuIQ.pdf" width="1212px" height="1200px" />'

    def day_pdf(self):
        return {
            "Mon": "01 PONDĚLÍ.pdf",
            "Tue": "02 ÚTERÝ.pdf",
            "Wed": "03 STŘEDA.pdf",
            "Thu": "04 ČTVRTEK.pdf",
            "Fri": '05 PÁTEK.pdf'
        }[self.today]
