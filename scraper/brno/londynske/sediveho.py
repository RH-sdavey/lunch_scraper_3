from scraper.Scraper import Scraper


class Sediveho(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todays_slice = {
            'Mon': slice(4, 11),
            'Tue': slice(12, 19),
            'Wed': slice(20, 27),
            'Thu': slice(28, 35),
            'Fri': slice(36, 43),
        }[self.today]

    def cleanup(self, daily_menu):
        result = []
        for item in daily_menu[self.todays_slice]:
            for dish in item._all_strings():
                if "&nbsp" not in dish:
                    result.append(dish)
        return result
