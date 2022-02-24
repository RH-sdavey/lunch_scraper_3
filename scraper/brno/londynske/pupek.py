from scraper.Scraper import Scraper


class Pupek(Scraper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        del daily_menu[0].contents[3].contents[3].contents[3]
        return daily_menu

