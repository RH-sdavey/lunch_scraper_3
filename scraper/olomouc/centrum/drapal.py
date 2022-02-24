from scraper.Scraper import PdfScraper


class Drapal(PdfScraper):
    def __init__(self, **kwargs):
        self.olo_drapal = 'olo_drapal.pdf'
        super().__init__(**kwargs)

    def scrape_data(self, **kwargs):
        return super(Drapal, self).scrape_data(self.olo_drapal)
