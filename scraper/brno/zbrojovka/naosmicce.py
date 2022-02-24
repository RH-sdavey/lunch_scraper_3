from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Naosmicce(PdfScraper):

    def __init__(self, city, district, restaurant, **kwargs):
        _ = kwargs
        self.data = restaurant_data(city, district, restaurant)
        self.brno_osmicce = "brno_osmicce.pdf"
        super().__init__(self.data.name, self.data.url)

    def scrape_data(self, **kwargs):
        return super(Naosmicce, self).scrape_data(self.brno_osmicce)
