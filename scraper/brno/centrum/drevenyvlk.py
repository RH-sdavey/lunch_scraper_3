from data.Data import restaurant_data


class Drevenyvlk:

    def __init__(self, city, district, restaurant, **kwargs):
        _ = kwargs
        self.data = restaurant_data(city, district, restaurant)

    @staticmethod
    def scrape_data():
        return '<iframe src="https://www.zomato.com/widgets/daily_menu.php?' \
               'entity_id=16507597&amp;width=100%&amp;height=700&quot;"' \
               ' width="100%" height="700" frameborder="0">' \
               '</iframe>'

    def cleanup(self, daily_menu):
        pass
