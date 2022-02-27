from scraper.Scraper import Scraper


class Tenmanya(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data(**kwargs):
        return '<img src="/static/assets/pdfs_sites/t1.jpg"/>' \
               '<img src="/static/assets/pdfs_sites/t2.jpg"/>' \
               '<img src="/static/assets/pdfs_sites/t3.jpg"/>' \


    def cleanup(self, daily_menu):
        return daily_menu
