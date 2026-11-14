from ...scraper import ImageScraper


class UStura(ImageScraper, id="u-stura"):
    """Posts the lunch menu as a picture (e.g. listopad2.png) on its own 'Polední menu' page."""
    name = "Restaurace U Šťura"
    city, area = "Kravaře", "near Štěpánkovice"
    url = "https://www.restauraceustura.cz/poledniacute-menu"
