from scraper.Scraper import Scraper


class Uhavlu(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        return f'<div class="col-md-12">{daily_menu}</div>'
