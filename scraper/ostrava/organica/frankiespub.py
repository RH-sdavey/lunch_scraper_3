from scraper.Scraper import Scraper


class Frankiespub(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        del daily_menu[1:]
        return daily_menu