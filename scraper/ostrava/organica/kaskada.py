from scraper.Scraper import Scraper


class Kaskada(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data(**kwargs):
        return '<iframe src="https://kaskadarestaurant.cz/ostrava_nova_karolina/menu/#my-tabs|0"' \
               ' width="100%" height="700" frameborder="0">' \
               '</iframe>'

    def cleanup(self, daily_menu):
        return