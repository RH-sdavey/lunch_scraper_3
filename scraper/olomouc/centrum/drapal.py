from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Drapal(PdfScraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        self.olo_drapal = 'olo_drapal.pdf'

        super().__init__(self.data.name, self.data.url)

    def scrape_data(self, **kwargs):
        return super(Drapal, self).scrape_data(self.olo_drapal)
