from scraper.Scraper import Scraper


class Padowetz(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todays_slice = {
            'Mon': 0,
            'Tue': 1,
            'Wed': 2,
            'Thu': 3,
            'Fri': 4,
        }[self.today]

    def cleanup(self, daily_menu):
        daily_menu = daily_menu[self.todays_slice]
        del daily_menu.contents[0]
        del daily_menu.contents[0].contents[0:2]
        del daily_menu.contents[2]
        del daily_menu.contents[3:]
        return daily_menu
