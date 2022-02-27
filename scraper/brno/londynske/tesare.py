from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Tesare(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return daily_menu

