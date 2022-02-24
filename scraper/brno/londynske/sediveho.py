from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Sediveho(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        super().__init__(self.data.name, self.data.url, self.data.html_section, **kwargs)

    def scrape_data(self):
        daily_menu = self.daily_menu_from_soup_object()
        return self.cleanup(daily_menu)

    def todays_slice(self):
        return {
            'Mon': slice(4, 11),
            'Tue': slice(12, 19),
            'Wed': slice(20, 27),
            'Thu': slice(28, 35),
            'Fri': slice(36, 43),
        }[self.today]

    def cleanup(self, daily_menu):
        result = []
        for item in daily_menu[self.todays_slice()]:
            for dish in item._all_strings():
                if "&nbsp" not in dish:
                    result.append(dish)
        return result
