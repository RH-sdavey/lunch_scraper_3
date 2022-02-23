import importlib
from datetime import datetime

from flask import Flask, render_template

from data.Data import data_dict, city_data, district_data, restaurant_data
from scraper.Scraper import Scraper

lunch_scraper_3 = Flask(__name__)

gbl = globals()


@lunch_scraper_3.route('/')
@lunch_scraper_3.route('/index.html')
@lunch_scraper_3.route('/home.html')
def index_route():
    """City names and descriptions"""
    return render_template('home.html', card_data=data_dict())


@lunch_scraper_3.route('/<string:city>')
def city_route(city):
    city = city_data(city)
    return render_template('city.html', city=city)


# @lunch_scraper_3.route('/test')
# def test_route():
#     """http://127.0.0.1:5000/test?restaurant=brno"""
#     city = request.args.get("restaurant")
#     city = city_data(city)
#     return render_template('index4.html', city=city)


@lunch_scraper_3.route('/<string:city>/<string:district>')
def district_route(city, district):
    district = district_data(city, district)
    return render_template('district.html',
                           city=city,
                           district=district)


@lunch_scraper_3.route('/<string:city>/<string:district>/<string:restaurant>')
def restaurant_route(city, district, restaurant):
    today = datetime.now().ctime().split()[0]
    if today in ['Sat', 'Sun']:
        return render_template('weekend.html')
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
    if type(daily_menu) == str:
        return render_template('restaurantPDF.html',
                           city=city,
                           district=district,
                           restaurant=restaurant,
                           restaurant_data=rest_data,
                           daily_menu=daily_menu)

    return render_template('restaurant.html',
                           city=city,
                           district=district,
                           restaurant=restaurant,
                           restaurant_data=rest_data,
                           daily_menu=daily_menu)



if __name__ == '__main__':
    lunch_scraper_3.run(debug=True)
