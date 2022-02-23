from dataclasses import dataclass
from typing import Optional


@dataclass
class Restaurant:
    name: str
    url: str
    description: str
    public_name: str
    html_section: Optional[dict | list | tuple | set]


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
        description='Lovely city in Moravia',
        districts=[
            District(
                name="londynske",
                restaurants=[
                    Restaurant(
                        name='mitrovski',
                        public_name="Mitrovski",
                        url="https://www.mitrovski.cz/menu/",
                        description="Small restaurant close to SQUARE HERE",
                        html_section=('div', {'class': 'sw-c section-wrapper-content cf'})
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
                    # Restaurant(
                    #     name='babeta',
                    #     url="https://www.restauraceunion.cz/tydenni-menu",
                    #     description="Union",
                    #     html_section=('div', {'id': 'phocamenu'})
                    #     ),
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
                        public_name="U Tesare (TODO)",
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
                        public_name="U stredoveka krcma (TODO)",
                        url="https://stredovekakrcma.cz/denni-menu/",
                        description="Medieval themed rest in Brnop",
                        html_section=('div', {'class': 'et_pb_section_1'})
                        ),
                    Restaurant(
                        name='mamut',
                        public_name="Mamut",
                        url="https://www.mamut-pub.cz/cz/page/nabidka.html",
                        description="njlkfedjnwefjnk",
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
                        name='continental',
                        public_name="Hotel Continental",
                        url="https://www.continentalbrno.cz/",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    Restaurant(
                        name='morgal',
                        public_name="Morgal",
                        url="https://www.morgal.cz/aktualni-nabidka-jidel",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'class': 'jidlobox'})
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
                        html_section=('div', {'id': 'wrapper'})
                        ),
                    Restaurant(
                        name='padowetz',
                        public_name="Padowetz",
                        url="http://www.restaurant-padowetz.cz/poledni-menu.htm",
                        description="njlkfedjnwefjnk",
                        html_section=('div', {'class': 'tydeniMenu'})
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
                        url="https://www.kolkovna.cz/cs/stopkova-plzenska-pivnice-16/denni-menu",
                        description="Very nice goose",
                        html_section=('div', {'class': 'dailyMenuWeek'})
                        ),
                    Restaurant(
                        name='jednabasen',
                        public_name="Jedna Basen",
                        url="https://jedna-basen.cz/#",
                        description="dwdwdwdwdwdwdw",
                        html_section=('div', {'data-id': '066527c'})
                        ),
                    Restaurant(
                        name='jasminabistro',
                        public_name="Jasmina Bistro",
                        url="https://jasminabistro.webnode.cz/menu/",
                        description="dwdwdwdwdwdwdw",
                        html_section=('div', {'class': 'section-wrapper-content'})
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
                        url="http://www.naosmicce.cz/",
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
        description='Lovely city in olomouc',
        districts=[
            District(
                name="centrum",
                restaurants=[
                    Restaurant(
                        name='potrefenahusa',
                        public_name="Potrefena Husa",
                        url="https://www.husa-olomouc.cz/cz/jidelni-listek/poledni-menu/",
                        description="a fine place",
                        html_section=('table', {'class': 'jidlo'})
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
                        name='soupka',
                        public_name="Soupka",
                        url="https://www.soupka.cz/",
                        description="Odwdwdswdwdwdw",
                        html_section=('div', {'class': 'jXK9ad-SmKAyb'})
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
                        url="http://www.morgansrestaurant.cz/wp-content/uploads/",
                        description="wdwdw",
                        html_section=('div', {'fake': 'fake'})
                        ),
                    ]
                )
            ]
        ),
    'ostrava': City(
        name='ostrava',
        description='lovely ostrava',
        districts=[
            District(
                name="centrum",
                restaurants=[
                    Restaurant(
                        name='makalu',
                        public_name="Mitrovski",
                        url="http://www.nepalska-restaurace-makalu.cz/ostrava.php",
                        description="Indian Restaurant with Mix Thali dishes",
                        html_section=('div', {'id': 'T_menu'})
                        )
                    ]
                )
            ]
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
