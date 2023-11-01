from scraper.Scraper import Scraper


class Drevenyvlk(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def scrape_data(**kwargs):
        return '<iframe src="https://www.zomato.com/widgets/daily_menu.php?' \
               'entity_id=16507597&amp;width=100%&amp;height=700&quot;"' \
               ' width="100%" height="700" frameborder="0">' \
               '</iframe>'

    def cleanup(self, daily_menu):
        return daily_menu
