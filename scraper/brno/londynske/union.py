from scraper.Scraper import Scraper


class Union(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        result = []
        for item in daily_menu[0].contents[1:16]:
            for dish in item._all_strings():
                if "\xa0" not in str(dish):
                    result.append(dish)
        return result


