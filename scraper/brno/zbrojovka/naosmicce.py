from scraper.Scraper import PdfScraper


class Naosmicce(PdfScraper):

    def __init__(self, **kwargs):
        self.brno_osmicce = "brno_osmicce.pdf"
        super().__init__(**kwargs)

    def scrape_data(self, **kwargs):
        return super(Naosmicce, self).scrape_data(self.brno_osmicce)
