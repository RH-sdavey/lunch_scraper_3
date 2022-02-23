from scraper.Scraper import Scraper
from data.Data import restaurant_data


class Union(Scraper):
    def __init__(self, city, district, restaurant, **kwargs):
        self.data = restaurant_data(city, district, restaurant)
        self.today = kwargs.get('today')

        super().__init__(self.data.name, self.data.url, self.data.html_section)

    def scrape_data(self):
        daily_menu = self.daily_menu_from_soup_object()
        return self.cleanup(daily_menu)

    def cleanup(self, daily_menu):
        result = []
        for item in daily_menu[0].contents[1:16]:
            for dish in item._all_strings():
                if "\xa0" not in str(dish):
                    result.append(dish)
        return result


