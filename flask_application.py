import importlib
from datetime import datetime
from pprint import pprint

from flask import Flask, render_template

from data.Data import data_dict, city_data, district_data

lunch_scraper_3 = Flask(__name__)

gbl = globals()


@lunch_scraper_3.route('/')
@lunch_scraper_3.route('/index.html')
@lunch_scraper_3.route('/home.html')
def index_route():
    """Route for home page"""
    return render_template(
        'home.html',
        card_data=data_dict()
    )


@lunch_scraper_3.route('/<string:city>')
def city_route(city):
    """Route for any city page (eg: /brno)"""
    city = city_data(city)
    scraped_totals = get_scraped_totals(city)
    return render_template(
        'city.html',
        city=city,
        scraped_totals=scraped_totals
    )


@lunch_scraper_3.route('/<string:city>/<string:district>')
def district_route(city, district):
    """Route for any district page (eg: /brno/londynske)"""
    district = district_data(city, district)
    return render_template(
        'district.html',
        city=city,
        district=district
    )


@lunch_scraper_3.route('/<string:city>/<string:district>/<string:restaurant>')
def restaurant_route(city, district, restaurant):
    """Route for any restaurant page (eg: /brno/londynske/pupek)"""
    today = datetime.now().ctime().split()[0]
    if today in ['Sat', 'Sun']:
        return render_template('weekend.html')
    daily_menu, rest_data = init_restaurant_module(city, district, restaurant, today)
    template_name_or_list = 'restaurantPDF.html' if type(daily_menu) == str else 'restaurant.html'
    return render_template(
        template_name_or_list=template_name_or_list,
        city=city,
        district=district,
        restaurant=restaurant,
        restaurant_data=rest_data,
        daily_menu=daily_menu
    )


def init_restaurant_module(*args):
    """Dynamically load the restaurant scraper module

    :return: scraped denni menu, restaurant data
    :rtype: tuple
    """
    city, district, restaurant, today = args
    module = f'scraper.{city}.{district}.{restaurant}'
    gbl[module] = importlib.import_module(module)

    module = gbl[module].__dict__[restaurant.capitalize()](
        city=city,
        district=district,
        restaurant=restaurant,
        today=today
    )
    # pprint(f"MODULE: {module}")
    return module.scrape_data(), module.data



def get_scraped_totals(city):
    districts = len(city.districts)
    restaurants = sum([len(district.restaurants) for district in city.districts])
    return districts, restaurants


if __name__ == '__main__':
    lunch_scraper_3.run(debug=True)
