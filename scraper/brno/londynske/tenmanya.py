import wget

from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Tenmanya:

    def __init__(self, city, district, restaurant, **kwargs):
        _ = kwargs
        self.data = restaurant_data(city, district, restaurant)

    @staticmethod
    def scrape_data():
        return '<img src="/static/assets/pdfs_sites/t1.jpg"/>' \
               '<img src="/static/assets/pdfs_sites/t2.jpg"/>' \
               '<img src="/static/assets/pdfs_sites/t3.jpg"/>' \

