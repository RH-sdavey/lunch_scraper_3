from scraper.Scraper import PdfScraper


class Drapal(PdfScraper):
    def __init__(self, **kwargs):
        self.olo_drapal = 'olo_drapal.pdf'
        super().__init__(**kwargs)

    def scrape_data(self, **kwargs):
        return '<embed src="http://www.restauracedrapal.cz/dennimenu.pdf" width="1212px" height="1200px" />'
