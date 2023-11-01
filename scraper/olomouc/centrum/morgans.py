from scraper.Scraper import Scraper


class Morgans(Scraper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        print(daily_menu)
        return daily_menu
