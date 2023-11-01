from scraper.Scraper import Scraper
import re


class Pivniburza(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def cleanup(self, daily_menu):
        hlavni_jidlo = str(daily_menu[2].contents[1].contents[1].contents[1])
        k_pivu = str(daily_menu[2].contents[1].contents[1].contents[3])
        return ["<div>", hlavni_jidlo, "<br/>", k_pivu, "</div>"]
