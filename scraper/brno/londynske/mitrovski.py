from scraper.Scraper import Scraper


class Mitrovski(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.day_path = {"Mon": 2, "Tue": 3, "Wed": 4, "Thu": 5, "Fri": 6}[self.today]

    def cleanup(self, daily_menu):
        return daily_menu[1].contents[self.day_path].contents[1].contents[1].contents[3]







