from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Potrefenahusa(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        super().__init__(self.data.name, self.data.url, self.data.html_section, **kwargs)

    def cleanup(self, daily_menu):
        return daily_menu

