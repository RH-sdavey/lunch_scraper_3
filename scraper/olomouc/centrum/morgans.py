from datetime import datetime

from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Morgans(PdfScraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        self.olo_morgans = 'olo-morgans.jpg'

        super().__init__(self.data.name, self.data.url)

    def scrape_data(self, **kwargs):
        day, month, full_month, year = self.get_dates_as_ints()
        custom_url = f'{year}/{full_month}/{day}.{month}.-web.jpg'
        return super(Morgans, self).scrape_data(self.olo_morgans, self.data.url + custom_url)

    @staticmethod
    def get_dates_as_ints():
        day = datetime.now().day
        month = datetime.now().month
        full_month = f"0{month}" if month < 10 else month
        year = datetime.now().year
        return day, month, full_month, year
