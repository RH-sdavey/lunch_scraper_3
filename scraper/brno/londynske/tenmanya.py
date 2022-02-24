from scraper.Scraper import Scraper


class Tenmanya(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def scrape_data(self):
        return '<img src="/static/assets/pdfs_sites/t1.jpg"/>' \
               '<img src="/static/assets/pdfs_sites/t2.jpg"/>' \
               '<img src="/static/assets/pdfs_sites/t3.jpg"/>' \


    def cleanup(self, daily_menu):
        pass
