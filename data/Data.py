from dataclasses import dataclass
from typing import Optional


@dataclass
class Restaurant:
    name: str
    url: str
    description: str
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
                        name='pupek',
                        url="pupek.com",
                        description="a fine place",
                        html_section=None
                    ),
                    Restaurant(
                        name='pupek2',
                        url="pupek2.com",
                        description="a fine place2",
                        html_section=None
                    ),
                ]
            ),
            District(
                name="centrum",
                restaurants=[
                    Restaurant(
                        name='sean',
                        url="sean",
                        description="sean",
                        html_section=None
                    ),
                    Restaurant(
                        name='centrumpupek2',
                        url="centrumpupek2.com",
                        description="centruma fine place2",
                        html_section=None
                    ),
                ]
            ),

        ]
    ),
    'olomouc': City(
        name='olomouc',
        description='Lovely city in olomouc',
        districts=[
            District(
                name="olomouclondynske",
                restaurants=[
                    Restaurant(
                        name='olomoucpupek',
                        url="olomoucpupek.com",
                        description="a fine place",
                        html_section=None
                    )
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
