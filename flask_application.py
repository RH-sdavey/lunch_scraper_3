import importlib
from datetime import datetime

from flask import Flask, render_template

from data.Data import data_dict, city_data, district_data, restaurant_data

lunch_scraper_3 = Flask(__name__)

gbl = globals()


@lunch_scraper_3.route('/')
@lunch_scraper_3.route('/index.html')
@lunch_scraper_3.route('/home.html')
def index_route():
    """City names and descriptions"""
    return render_template(
        'home.html',
        card_data=data_dict()
    )


@lunch_scraper_3.route('/<string:city>')
def city_route(city):
    city = city_data(city)
    scraped_totals = get_scraped_totals(city)
    return render_template(
        'city.html',
        city=city,
        scraped_totals=scraped_totals
    )


@lunch_scraper_3.route('/<string:city>/<string:district>')
def district_route(city, district):
    district = district_data(city, district)
    return render_template(
        'district.html',
        city=city,
        district=district
    )


@lunch_scraper_3.route('/<string:city>/<string:district>/<string:restaurant>')
def restaurant_route(city, district, restaurant):
    today = datetime.now().ctime().split()[0]
    i_dont_scrape_on_weekends(today)
    daily_menu, rest_data = init_restaurant_module(city, district, restaurant, today)
    if type(daily_menu) == str:  # static path to a pdf or img file
        return render_template(
            'restaurantPDF.html',
            city=city,
            district=district,
            restaurant=restaurant,
            restaurant_data=rest_data,
            daily_menu=daily_menu
        )

    return render_template(
        'restaurant.html',
        city=city,
        district=district,
        restaurant=restaurant,
        restaurant_data=rest_data,
        daily_menu=daily_menu
    )


def init_restaurant_module(city, district, restaurant, today):
    module = f'scraper.{city}.{district}.{restaurant}'
    gbl[module] = importlib.import_module(module)
    module = gbl[module].__dict__[restaurant.capitalize()](
        city=city,
        district=district,
        restaurant=restaurant,
        today=today
    )
    rest_data = restaurant_data(city, district, restaurant)
    daily_menu = module.scrape_data()
    return daily_menu, rest_data


def i_dont_scrape_on_weekends(today):
    if today in ['Sat', 'Sun']:
        return render_template('weekend.html')


def get_scraped_totals(city):
    districts = len(city.districts)
    restaurants = sum([len(district.restaurants) for district in city.districts])

    return districts, restaurants


if __name__ == '__main__':
    lunch_scraper_3.run(debug=True)
