from data.Data import restaurant_data


class Himalaya:

    def __init__(self, city, district, restaurant, **kwargs):
        _ = kwargs
        self.data = restaurant_data(city, district, restaurant)

    @staticmethod
    def scrape_data():
        return '<img src="/static/assets/pdfs_sites/himalaya.jpg"/>'
