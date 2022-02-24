from scraper.Scraper import PdfScraper


class Continental(PdfScraper):

    def __init__(self, **kwargs):
        self.brno_continental = "brno_continental.pdf"
        super().__init__(**kwargs)

    def scrape_data(self, **kwargs):
        return super(Continental, self).scrape_data(
            self.brno_continental,
            custom_url="https://www.continentalbrno.cz/wp-content/uploads/2021/11/jidelni-listek_2021.pdf"
        )
