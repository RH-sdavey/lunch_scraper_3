from scraper.Scraper import PdfScraper
from data.Data import restaurant_data


class Iqmoravka(PdfScraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        self.brno_IQ = "brno_IQ.pdf"

        super().__init__(self.data.name, self.data.url)

    def scrape_data(self, **kwargs):
        return super(Iqmoravka, self).scrape_data(self.brno_IQ, custom_url=self.data.url + self.day_pdf())

    def day_pdf(self):
        return {
            "Mon": "01 PONDĚLÍ.pdf",
            "Tue": "02 ÚTERÝ.pdf",
            "Wed": "03 STŘEDA.pdf",
            "Thu": "04 ČTVRTEK.pdf",
            "Fri": '05 PÁTEK.pdf'
        }[self.today]
