from data.Data import restaurant_data


class Ukamena:

    def __init__(self, city, district, restaurant, **kwargs):
        _ = kwargs
        self.data = restaurant_data(city, district, restaurant)

    @staticmethod
    def scrape_data():
        return '<img style="width: 30rem; height:30rem;" src="/static/assets/pdfs_sites/k1.jpg"/>' \
               '<img style="width: 30rem; height:30rem;" src="/static/assets/pdfs_sites/k2.jpg"/>' \
               '<img style="width: 30rem; height:30rem;" src="/static/assets/pdfs_sites/k3.jpg"/>' \
