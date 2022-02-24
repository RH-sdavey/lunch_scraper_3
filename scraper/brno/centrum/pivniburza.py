from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Pivniburza(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        super().__init__(self.data.name, self.data.url, self.data.html_section, **kwargs)

    def scrape_data(self):
        daily_menu = self.daily_menu_from_soup_object()
        return self.cleanup(daily_menu)

    def cleanup(self, daily_menu):
        return [
            "<div>", daily_menu[2].contents[1].contents[1].contents[1], "<br/>",
            daily_menu[2].contents[1].contents[1].contents[3], "</div>",
            ]
