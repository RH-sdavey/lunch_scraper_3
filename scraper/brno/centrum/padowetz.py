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
        return f'<div class="ml-2">{daily_menu}</div>'
