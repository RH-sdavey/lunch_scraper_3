from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Mitrovski(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        super().__init__(self.data.name, self.data.url, self.data.html_section, **kwargs)
        self.day_path = {"Mon": 2, "Tue": 3, "Wed": 4, "Thu": 5, "Fri": 6}[self.today]

    def cleanup(self, daily_menu):
        return [
            "<br/><br/>".join(item) for item in daily_menu[1].contents[
                    self.day_path
            ].contents[1].contents[1].contents[3].contents[1].contents[1].contents[2].contents[1].contents
        ]






