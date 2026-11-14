from ...scraper import EmbedScraper


class ObecniDumKoberice(EmbedScraper, id="obecni-dum-koberice"):
    """Their daily menu only exists in the Menicka.cz widget on their own page, so the card
    embeds that widget. Prices from their ordering site: menu 1/2/3 = 139/149/159 Kč, soup 20 Kč."""
    name = "Obecní dům Kobeřice"
    city, area = "Kobeřice", "near Štěpánkovice"
    url = "https://restauracekoberice.cz/denni-menu/"
    embed_url = "https://www.menicka.cz/api/iframe/?id=6942&size=16"
