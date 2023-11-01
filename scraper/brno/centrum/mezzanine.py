from scraper.Scraper import Scraper


class Mezzanine(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return daily_menu

    @staticmethod
    def scrape_data():
        return '<embed src="/static/assets/pdfs_sites/mezza.pdf" width="1212px" height="1200px" />'
