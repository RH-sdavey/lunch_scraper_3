from scraper.Scraper import Scraper
from bs4 import BeautifulSoup as Bs4
import datetime
import locale

class Charliessquare(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cleanup(self, daily_menu):
        weekly_menu = self.get_weekly_options(daily_menu)

        return (f"<div class='row col-lg-2' style='margin-left:15%'>"
                f"{self.get_soup_option(daily_menu, self.todays_date_in_czech())}"
                f"</div>"
                f"{weekly_menu}")

    def todays_date_in_czech(self):
        locale.setlocale(locale.LC_ALL, 'Czech')
        today = datetime.date.today()
        czech_date = today.strftime('%A %d. %m.').capitalize()
        return czech_date

    def get_soup_option(self, daily_menu, day):
        all_soups = self.soup.find('div', attrs={'class': 'menu-for-one-day'})
        return all_soups

    def get_weekly_options(self, daily_menu):
        soup = Bs4(str(daily_menu), 'html.parser')
        weekly_menu = []
        weekly_table = soup.find('table', class_='menu-to-week')
        if weekly_table:
            for tr in weekly_table.find_all('tr'):
                td_elements = tr.find_all('td')
                if len(td_elements) >= 2:
                    dish = td_elements[0].get_text(strip=True)
                    price = td_elements[1].get_text(strip=True)
                    weekly_menu.append(f"{dish} - {price}")
        html_list = '<ul>\n'
        for item in weekly_menu:
            html_list += f'  <li> {item} </li>\n'
        html_list += '</ul>'
        return html_list