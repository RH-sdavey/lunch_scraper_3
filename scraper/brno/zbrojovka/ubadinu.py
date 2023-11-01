from scraper.Scraper import Scraper


class Ubadinu(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return "This restaurant are clearly actively trying to stop any scrapers or api connections to their website, please just use the link above "
