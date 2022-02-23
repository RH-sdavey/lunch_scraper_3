from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Drevenyorel(Scraper):

    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')
        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        return '<iframe src="https://www.zomato.com/widgets/daily_menu.php?entity_id=16506896&amp;width=100%&amp;height=700&quot;" width="100%" height="700" frameborder="0"></iframe>'

    def cleanup(self, daily_menu):
        pass

