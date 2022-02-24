from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Pupek(Scraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        super().__init__(self.data.name, self.data.url, self.data.html_section, **kwargs)

    def cleanup(self, daily_menu):
        del daily_menu[0].contents[3].contents[3].contents[3]
        return daily_menu

