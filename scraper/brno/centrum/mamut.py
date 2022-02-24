from scraper.Scraper import Scraper


class Mamut(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return daily_menu
