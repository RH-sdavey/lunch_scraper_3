from scraper.Scraper import Scraper


class Sediveho(Scraper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todays_slice = {
            'Mon': slice(4, 11),
            'Tue': slice(12, 19),
            'Wed': slice(20, 27),
            'Thu': slice(28, 35),
            'Fri': slice(36, 43),
        }[self.today]

    def cleanup(self, daily_menu):
        # Find the elements containing the desired text
        start_text = "Ceník obědového menu včetně polévky:"
        end_text = "Restaurace U šedivého vola, Pekařská 80"

        # Find the starting and ending elements
        start_element = self.soup.find('p', text=start_text)
        end_element = self.soup.find('p', text=end_text)

        # Initialize a list to store the content
        menu_content = []

        # Iterate through the elements between start and end
        current_element = start_element
        while current_element is not None and current_element != end_element:
            menu_content.append(current_element.get_text())
            menu_content.append("<br/>")
            current_element = current_element.find_next('p')

        return self.parse_todays_menu(menu_content)

    def parse_todays_menu(self, menu_content):

        menu_dict = {}
        current_day = None
        current_menu = []

        for item in menu_content:
            # Check if the item starts with a day of the week in Czech
            if item.startswith("Pondělí") or item.startswith("Úterý") or item.startswith("Středa") or item.startswith(
                    "Čtvrtek") or item.startswith("Pátek"):
                if current_day is not None:
                    menu_dict[current_day.split(" ")[0]] = current_menu
                current_day = item.strip()
                current_menu = [item]
            else:
                current_menu.append(item)

        # Add the last day's menu to the dictionary
        if current_day is not None:
            menu_dict[current_day] = current_menu
        return menu_dict[self.lookup_today_en_to_cz()]

    def lookup_today_en_to_cz(self):
        lookup_en_to_cz = {
            'Mon': 'Pondělí',
            'Tues': 'Úterý',
            'Wed': 'Středa',
            'Thurs': 'Čtvrtek',
            'Fri': 'Pátek'
        }
        return lookup_en_to_cz[self.today]
