from scraper.Scraper import Scraper


class Pivniburza(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def cleanup(self, daily_menu):
        return [
            "<div>", daily_menu[2].contents[1].contents[1].contents[1], "<br/>",
            daily_menu[2].contents[1].contents[1].contents[3], "</div>",
        ]
