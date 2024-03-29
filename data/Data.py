from dataclasses import dataclass
from typing import Optional

# Comment to trigger deployment

@dataclass
class Restaurant:
    name: str
    url: str
    description: str
    public_name: str
    html_section: tuple


@dataclass
class District:
    name: str
    restaurants: list[Restaurant]


@dataclass
class City:
    name: str
    description: str
    districts: list[District]


data = {
    'brno': City(
        name='brno',
        description='Brno is a city in the South Moravian Region of the Czech Republic. Located at the confluence of the Svitava and Svratka rivers, Brno has about 380,000 inhabitants, making it the second-largest city in the Czech Republic after the capital, Prague, and one of the 100 largest cities of the EU.',
        districts=[
            District(
                name="londynske",
                restaurants=[
                    Restaurant(
                        name='mitrovski',
                        public_name="Mitrovski",
                        url="https://www.mitrovski.cz/menu/",
                        description="Small restaurant close to SQUARE HERE",
                        html_section=('div', {'class': 'sw-c cf'})
                        ),
                    Restaurant(
                        name='pupek',
                        public_name="Pupek",
                        url="https://www.uhovezihopupku.cz/menu/",
                        description="Excellent Service guaranteed",
                        html_section=('div', {'class': 'menu_dnes'})
                        ),
                    Restaurant(
                        name='sediveho',
                        public_name="U Sediveho Vola (TODO)",
                        url="https://www.usedivehovola.com/denni-obedove-menu",
                        description="U Sediveho Vola: close to SQUARE HERE",
                        html_section=('p', {'class': 'font_8'})
                        ),
                    Restaurant(
                        name='union',
                        public_name="Union",
                        url="https://www.restauraceunion.cz/tydenni-menu",
                        description="Union",
                        html_section=('div', {'id': 'phocamenu'})
                        ),
                    Restaurant(
                        name='iqmoravka',
                        public_name="IQ Moravka",
                        url="http://www.iqrestaurant.cz/moravka/",
                        description="IQ Moravka",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='tenmanya',
                        public_name="Tenmanya",
                        url="https://www.facebook.com/sushibrno/",
                        description="Running Sushi",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='tesare',
                        public_name="U Tesare",
                        url="http://www.utesare.cz/poledni-nabidka/",
                        description="Tesare",
                        html_section=('div', {'data-id': 'f96fb5e'})
                        ),
                    ]
                ),
            District(
                name="centrum",
                restaurants=[
                    Restaurant(
                        name='charliessquare',
                        public_name="Charlies Square",
                        url="https://www.charliessquare.cz/menu/",
                        description="Charielseslkels",
                        html_section=('div', {'class': 'entry-content'})
                        ),
                    Restaurant(
                        name='stredovekakrcma',
                        public_name="U stredoveka krcma (OBSOLETE?)",
                        url="https://stredovekakrcma.cz/denni-menu/",
                        description="""
                        Medieval themed rest in Brno
                        Possibly Obsolete
                        Website showing old data""",
                        html_section=('div', {'class': 'et_pb_section_1'})
                        ),
                    Restaurant(
                        name='mamut',
                        public_name="Mamut  (OBSOLETE?)",
                        url="https://www.mamut-pub.cz/cz/page/nabidka.html",
                        description="Bistro upstairs, Pull your own beer downstairs",
                        html_section=('section', {'id': 'content'})
                        ),
                    Restaurant(
                        name='mezzanine',
                        public_name="Mezzanine",
                        url="https://www.cafe-mezzanine.cz/",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'fake': 'fake'})
                        ),

                    Restaurant(
                        name='morgal',
                        public_name="Morgal",
                        url="https://www.morgal.cz/aktualni-nabidka-jidel",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'class': 'nabidkatext'})
                        ),
                    Restaurant(
                        name='skog',
                        public_name="Skog",
                        url="https://www.skog.cz/nabidka-jidla/",
                        description="njlkfedjnwefjnk",
                        html_section=('section', {'class': 'subpage-list'})
                        ),
                    Restaurant(
                        name='jpbistro',
                        public_name="Jean Pauls Bistro (Zelny Trh)",
                        url="https://www.jpbistro.cz/menu-ztrh/index.php",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='padowetz',
                        public_name="Padowetz",
                        url="https://restaurant-padowetz.cz/poledni-menu",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'class': 'col-md-7'})
                        ),
                    Restaurant(
                        name='pivniburza',
                        public_name="Pivni Burza",
                        url="https://pivniburza.cz/jidelni-listek/",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'class': 'container'})
                        ),
                    Restaurant(
                        name='drevenyvlk',
                        public_name="U Dreveneho Vlka (TODO)",
                        url="http://www.drevenyvlk.cz/cz/page/tydenni-menu.html",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='drevenyorel',
                        public_name="U Dreveneho Orla (TODO)",
                        url="http://drevenyorel.cz/cz/page/tydenni-menu.html",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='stopkova',
                        public_name="Stopkova Kolkvona Pivnice",
                        url="https://stopkova.kolkovna.cz/#poledni-menu",
                        description="Very nice goose",
                        html_section=('div', {'class': 'food-list-daily'})
                        ),
                    Restaurant(
                        name='jednabasen',
                        public_name="Jedna Basen",
                        url="https://jedna-basen.cz/#",
                        description="dwdwdwdwdwdwdw",
                        html_section=('div', {'data-id': '066527c'})
                        ),
                    Restaurant(
                        name='himalaya',
                        public_name="Himalaya Indicka Restaurace",
                        url="https://www.himalayarestaurace.cz/denni-menu/",
                        description="dwdwdwdwdwdwdw",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='pavilion',
                        public_name="Pavilion Steak House",
                        url="https://pavillonsteakhouse.cz/obedove-menu/",
                        description="dwdwdwdwdwdwdw",
                        html_section=('div', {'class': 'et_pb_image_1'})
                        ),
                    ]
                ),
            District(
                name="zbrojovka",
                restaurants=[
                    Restaurant(
                        name='musilce',
                        public_name="Musilce",
                        url="https://www.menicka.cz/5400-restaurace-na-musilce.html#m",
                        description="jnfenokwf",
                        html_section=('div', {'class': 'menicka'})
                        ),
                    Restaurant(
                        name='onyx',
                        public_name="Onyx",
                        url="https://www.menicka.cz/6722-restobar-onyx.html#m",
                        description="jnfenokwf",
                        html_section=('div', {'class': 'menicka'})
                        ),
                    Restaurant(
                        name='naosmicce',
                        public_name="Na Osmicce",
                        url="http://www.naosmicce.cz/Menu.pdf",
                        description="jnfenokwf",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='svitavskarychta',
                        public_name="Svitavska Rychta",
                        url="http://www.svitavskarychta.cz/tydenni-menu/",
                        description="jnfenokwf",
                        html_section=('div', {'class': 'entry'})
                        ),
                    Restaurant(
                        name='ubadinu',
                        public_name="U Badina",
                        url="http://www.ubadinu.cz/denni-menu-1.html",
                        description="jnfenokwf",
                        html_section=('div', {'class': 'novinkatext'})
                        ),
                    ]
                )
            ]
        ),
    'olomouc': City(
        name='olomouc',
        description='Olomouc has about 100,000 inhabitants, and its larger urban zone has a population of about 384,000 inhabitants.',
        districts=[
            District(
                name="centrum",
                restaurants=[
                    Restaurant(
                        name='potrefenahusa',
                        public_name="Potrefena Husa",
                        url="https://www.husa-olomouc.cz/cz/jidelni-listek/poledni-menu/",
                        description="a fine place",
                        html_section=('div', {'class': 'main'})
                        ),
                    Restaurant(
                        name='moravskarestaurace',
                        public_name="Moravska Restaurace",
                        url="https://www.moravskarestaurace.cz/menu",
                        description="Overpriced and unfriendly",
                        html_section=('div', {'class': 'meals-container__inner'})
                        ),
                    Restaurant(
                        name='drapal',
                        public_name="Drápal",
                        url="http://www.restauracedrapal.cz/dennimenu.pdf",
                        description="Odwdwdw",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='kozlovnam3',
                        public_name="Kozlovna M3",
                        url="https://www.kozlovnam3.cz/tydenni-menu/",
                        description="Odwdwdswwdwdwdwdwdwdwdw",
                        html_section=('div', {'class': 'entry-content'})
                        ),
                    Restaurant(
                        name='morgans',
                        public_name="Morgans Restaurant",
                        url="https://www.morgansrestaurant.cz/en/lunch-menu/",
                        description="wdwdw",
                        html_section=('figure', {'class': 'wp-block-image'})
                        ),
                    ]
                ),
            District(
                name="svatykopecek",
                restaurants=[
                    Restaurant(
                        name='umacku',
                        public_name="Restaurace U Macků",
                        url="http://www.restauraceumacku.cz/?section=denni-menu",
                        description="Nice comfortable bar with friendly staff",
                        html_section=('div', {'class': 'obsah'})
                    ),
                    Restaurant(
                        name='ukamena',
                        public_name="U Kameňa",
                        url="http://ukamena.webmium.com/jidelnicek",
                        description="One of the best bars in whole CZ, perfect",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='umaci',
                        public_name="Hospůdka U Maci",
                        url="http://www.hospudkaumaci.cz/jidelni-listek/",
                        description="Beautiful local bar close to Olomouc Zoo",
                        html_section=('div', {'class': 'post-content'})
                        ),
                    Restaurant(
                        name='uhavlu',
                        public_name="Hostinec u Havlů",
                        url="https://www.uhavlu.cz/jidelni-listek/",
                        description="Bdwdwdwdw",
                        html_section=('div', {'class': 'group'})
                        ),
                ],
            ),
        ],
        ),
    'ostrava': City(
        name='ostrava',
        description='Ostrava is the capital of the Moravian-Silesian Region. It has about 285,000 inhabitants. It lies 15 km (9 mi) from the border with Poland, at the confluences of four rivers: Oder, Opava, Ostravice and Lučina. Ostrava is the third largest city in the Czech Republic.',
        districts=[
            District(
                name="organica",
                restaurants=[
                    Restaurant(
                        name='frankiespub',
                        public_name="Frankies Pub",
                        url="https://www.menicka.cz/7080-frankies-pub.html",
                        description="Very friendly staff, directly opposite Organica",
                        html_section=('div', {'class': 'menicka'})
                        ),
                    Restaurant(
                        name='moravskachalupa',
                        public_name="Moravska chalupa",
                        url="https://www.moravskachalupa.cz/denni-menu",
                        description="Looks good",
                        html_section=('div', {'class': 'denni-menu'})
                    ),
                    Restaurant(
                        name='guest',
                        public_name="Guest Restaurant",
                        url="http://www.guest-restaurant.com/",
                        description="Looks overpriced and pretentious",
                        html_section=('div', {'class': 'gk-cols'})
                    ),
                    Restaurant(
                        name='kaskada',
                        public_name="Kaskada Restaurant",
                        url="https://kaskadarestaurant.cz/",
                        description="",
                        html_section=('div', {'fake': 'fake'})
                    ),
                    Restaurant(
                        name='yasmine',
                        public_name="Yasmine Kebab and Grill",
                        url="https://www.yasminekebabgrill.cz/",
                        description="",
                        html_section=('div', {'fake': 'fake'})
                    ),
                    Restaurant(
                        name='knossos',
                        public_name="Knossos Restaurant",
                        url="http://www.knossos-restaurant.cz/",
                        description="",
                        html_section=('div', {'class': 'box-white'})
                    ),
                    Restaurant(
                        name='urady',
                        public_name="Restaurace U Rady",
                        url="https://restauraceurady.cz/",
                        description="Needs to be updated manually (for now)",
                        html_section=('div', {'fake': 'fake'})
                    ),
                    Restaurant(
                        name='septim',
                        public_name="Restaurace Septim",
                        url="https://restaurace-pizzerie-kavarna.com/restaurace_septim/modern/menicko_denni_menu/menicko_denni_menu.php",
                        description="",
                        html_section=('table', {'cellpadding': '4'})
                    ),
                    Restaurant(
                        name='paleta',
                        public_name="Paleta Restaurace",
                        url="https://www.paletarestaurant.cz/menu/menu.php",
                        description="Check this daily(might need to add day-slicing)",
                        html_section=('table', {'class': 'meals-daily'})
                    ),

                ]
                ),
            District(
                name="stodolni",
                restaurants=[
                    Restaurant(
                        name='slezska',
                        public_name="Slezska",
                        url="https://www.slezska.com/?#poledni_menu",
                        description="Check this daily(might need to add day-slicing)",
                        html_section=('div', {'id': 'antilukas'})
                    ),
                ]
            )
        ],
    ),
}


def data_dict():
    return data


def city_data(city):
    return data[city]


def district_data(city, district):
    city = city_data(city)
    return [_ for _ in city.districts if _.name == district][0]


def restaurant_data(city, district, restaurant):
    city = city_data(city)
    district = [_ for _ in city.districts if _.name == district][0]
    return [_ for _ in district.restaurants if _.name == restaurant][0]
