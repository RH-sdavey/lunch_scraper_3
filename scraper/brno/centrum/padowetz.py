from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Padowetz(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        print(self.data)
        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        daily_menu = self.daily_menu_from_soup_object()
        daily_menu = daily_menu[self.todays_slice()]
        return self.cleanup(daily_menu)

    def todays_slice(self):
        return {
            'Mon': 0,
            'Tue': 1,
            'Wed': 2,
            'Thu': 3,
            'Fri': 4,
        }[self.today]

    def cleanup(self, daily_menu):
        del daily_menu.contents[0]
        del daily_menu.contents[0].contents[0:2]
        del daily_menu.contents[2]
        del daily_menu.contents[3:]
        return daily_menu
