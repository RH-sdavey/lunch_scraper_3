from scraper.Scraper import Scraper


class Continental(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return daily_menu

    @staticmethod
    def scrape_data(**kwargs):
        return '<embed src="/static/assets/pdfs_sites/continental_brno.pdf" width="1212px" height="1200px" />'
