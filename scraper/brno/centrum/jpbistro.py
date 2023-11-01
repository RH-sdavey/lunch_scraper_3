from scraper.Scraper import Scraper


class Jpbistro(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data():
        return '<embed src="https://www.jpbistro.cz/assets/menu/obed-menu/obed-zelnytrh.pdf" width="1212px" height="1200px" />'

    def cleanup(self, daily_menu):
        return daily_menu
