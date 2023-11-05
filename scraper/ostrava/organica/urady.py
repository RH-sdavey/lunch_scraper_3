from scraper.Scraper import Scraper


class Urady(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data(**kwargs):
        return '<iframe src="https://restauraceurady.cz/wp-content/uploads/2023/10/Menu-30.10.-3.11.2023.pdf"' \
               ' width="100%" height="700" frameborder="0">' \
               '</iframe>'

    def cleanup(self, daily_menu):
        return