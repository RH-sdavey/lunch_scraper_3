from scraper.Scraper import Scraper


class Chalupa(Scraper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def scrape_data(self):
        return '<img src="/static/assets/pdfs_sites/chalupa.jpg"/>'

    def cleanup(self):
        ...
