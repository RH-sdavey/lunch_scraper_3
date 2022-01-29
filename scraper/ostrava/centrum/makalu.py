from pprint import pprint

from scraper.Scraper import Scraper
from data.Data import restaurant_data
from bs4 import BeautifulSoup as bs4
from bs4.element import Tag
import soupsieve as sv



class Makalu(Scraper):
    def __init__(self, city, district, restaurant):
        self.data = restaurant_data(city, district, restaurant)
        print(self.data)
        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        daily_menu = self.daily_menu_from_soup_object()

        return self.cleanup(daily_menu)

    def cleanup(self, daily_menu):
        result = []
        out = []
        pprint(daily_menu)
        pprint(type(daily_menu))
        pprint(len(daily_menu))
        for side in daily_menu.contents[1:3]:
            for content in side.contents:
                if isinstance(content, Tag) and content.contents:
                    result.append(content)
        # for side in daily_menu:
        #     for item in side:
        #         result.append(item)
        # for item in result:
        #     if item.text and isinstance(item, Tag):

        #         out.append(item)

        # result = sv.select('div:is(.TJStrana)', daily_menu[0])
        # result = sv.filter('img:not(TJnadpis)', result)
        # print(result)
        pprint(result)
        return result

    # # def cleanup(self, daily_menu):
    # #     pprint(daily_menu[0])
    # #     return [i for i in daily_menu]
