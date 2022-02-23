from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Mitrovski(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        print(self.data)
        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        daily_menu = self.daily_menu_from_soup_object()
        return ["<br/><br/>".join(item) for item in self.cleanup(daily_menu)]

    def day_path(self, today):
        day_paths = {"Mon": 2, "Tue": 3, "Wed": 4, "Thu": 5, "Fri": 6}
        return day_paths[today]

    def cleanup(self, daily_menu):
        return daily_menu[1].contents[self.day_path(self.today)].contents[1].contents[1].contents[3].contents[1].contents[1].contents[2].contents[1].contents






