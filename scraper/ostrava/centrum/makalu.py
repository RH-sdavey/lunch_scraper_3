import bs4

from scraper.Scraper import Scraper
from data.Data import restaurant_data
from bs4.element import Tag, NavigableString


class Makalu(Scraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        print(self.data)
        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        result = []
        daily_menu = self.daily_menu_from_soup_object()
        for item in self.cleanup(daily_menu):
            result.append(item)
        return result

    def cleanup(self, daily_menu):
        unwanted = [

        ]
        for tag in daily_menu:
            for desc in tag.descendants:
                if desc not in unwanted:
                    print(f"TYPE {type(desc)}: HERE --> {desc}")
                yield desc


