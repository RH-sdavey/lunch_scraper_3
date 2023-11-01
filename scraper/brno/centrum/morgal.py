from scraper.Scraper import Scraper


class Morgal(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def cleanup(self, daily_menu):
        daily_menu = str(daily_menu).replace('<img class="off" src="http://www.morgal.cz/images/art_thumb/131/_thumb3/kucharipaprika.jpg"/>', '')
        return daily_menu
