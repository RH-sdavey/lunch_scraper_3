from scraper.Scraper import Scraper


class Chalupa(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data(**kwargs):
        return '<img src="/static/assets/pdfs_sites/chalupa.jpg"/>'

    def cleanup(self, daily_menu):
        return daily_menu
