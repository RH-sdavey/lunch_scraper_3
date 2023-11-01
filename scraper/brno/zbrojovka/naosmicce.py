from scraper.Scraper import PdfScraper


class Naosmicce(PdfScraper):

    def __init__(self, **kwargs):
        self.brno_osmicce = "brno_osmicce.pdf"
        super().__init__(**kwargs)

    def scrape_data(self, **kwargs):
        return '<embed src="http://www.naosmicce.cz/Menu.pdf" width="1212px" height="1200px" />'

