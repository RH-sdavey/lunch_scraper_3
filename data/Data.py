from dataclasses import dataclass

@dataclass
class Restaurant:
    name: str
    website: str
    description: str


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
                        website="pupek.com",
                        description="a fine place"
                    ),
                    Restaurant(
                        name='pupek2',
                        website="pupek2.com",
                        description="a fine place2"
                    ),
                ]
            ),
            District(
                name="centrum",
                restaurants=[
                    Restaurant(
                        name='sean',
                        website="sean",
                        description="sean"
                    ),
                    Restaurant(
                        name='centrumpupek2',
                        website="centrumpupek2.com",
                        description="centruma fine place2"
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
                        website="olomoucpupek.com",
                        description="a fine place"
                    )
                ]
            )
        ]
    ),
    'prague': City(
        name='prague',
        description='Lovely city in prague',
        districts=[
            District(
                name="praguelondynske",
                restaurants=[
                    Restaurant(
                        name='praguepupek',
                        website="praguepupek.com",
                        description="a fine place"
                    )
                ]
            )
        ]
    ),
}


def data_dict():
    return data


def get_data_for_(city):
    return data[city]
