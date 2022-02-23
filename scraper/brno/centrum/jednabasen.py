from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Jednabasen(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        return self.daily_menu_from_soup_object()

    def cleanup(self, daily_menu):
        pass

