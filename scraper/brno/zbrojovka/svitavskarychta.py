from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Svitavskarychta(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        daily_menu = self.daily_menu_from_soup_object()
        return self.cleanup(daily_menu)

    def cleanup(self, daily_menu):
        return daily_menu

