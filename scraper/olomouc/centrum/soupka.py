from scraper.Scraper import Scraper


class Soupka(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return daily_menu
