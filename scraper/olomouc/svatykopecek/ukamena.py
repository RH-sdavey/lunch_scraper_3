
from scraper.Scraper import Scraper


class Ukamena(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def scrape_data(self):
        return '<img style="width: 30rem; height:30rem;" src="/static/assets/pdfs_sites/k1.jpg"/>' \
               '<img style="width: 30rem; height:30rem;" src="/static/assets/pdfs_sites/k2.jpg"/>' \
               '<img style="width: 30rem; height:30rem;" src="/static/assets/pdfs_sites/k3.jpg"/>'

    def cleanup(self, **kwargs):
        ...
