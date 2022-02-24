from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Onyx(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        super().__init__(self.data.name, self.data.url, self.data.html_section, **kwargs)

    def cleanup(self, daily_menu):
        daily_menu = daily_menu[0]
        return [
            "<div>",
            daily_menu.contents[1].contents[0],
            "<br/>",
            daily_menu.contents[3].contents[1].contents[1],
            daily_menu.contents[3].contents[7].contents[1].contents[1],
            daily_menu.contents[3].contents[7].contents[3].contents[0],
            daily_menu.contents[3].contents[9].contents[1].contents[1],
            daily_menu.contents[3].contents[9].contents[3].contents[0],
            daily_menu.contents[3].contents[11].contents[1].contents[1],
            daily_menu.contents[3].contents[11].contents[3].contents[0],
            daily_menu.contents[3].contents[13].contents[1].contents[1],
            daily_menu.contents[3].contents[13].contents[3].contents[0],
            daily_menu.contents[3].contents[15].contents[1].contents[1],
            daily_menu.contents[3].contents[15].contents[3].contents[0],
            "</div>"
            ]


