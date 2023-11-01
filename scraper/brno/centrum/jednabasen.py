from scraper.Scraper import Scraper


class Jednabasen(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data():
        return '<embed src="https://www.jedna-basen.cz/denni-menu/#streda" width="1212px" height="1200px" />'

    def cleanup(self, daily_menu):
        return daily_menu
