from scraper.Scraper import Scraper


class Yasmine(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data(**kwargs):
        return '<img style="width: 120rem; height:100rem;" src="/static/assets/pdfs_sites/yasmine.jpg"/>'

    def cleanup(self, daily_menu):
        return