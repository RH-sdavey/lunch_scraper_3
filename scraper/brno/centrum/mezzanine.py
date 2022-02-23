import wget

from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Mezzanine:

    def __init__(self, city, district, restaurant, **kwargs):
        _ = kwargs
        self.data = restaurant_data(city, district, restaurant)

    def scrape_data(self):
        return '<embed src="/static/assets/pdfs_sites/mezza.pdf" width="1212px" height="1200px" />'

