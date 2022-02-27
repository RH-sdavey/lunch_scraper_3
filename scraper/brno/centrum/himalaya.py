from scraper.Scraper import Scraper


class Himalaya(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return daily_menu

    @staticmethod
    def scrape_data(**kwargs):
        return '<img src="/static/assets/pdfs_sites/himalaya.jpg"/>'
