from flask import Flask, render_template

from data.Data import data_dict, get_data_for_

lunch_scraper_3 = Flask(__name__)


@lunch_scraper_3.route('/')
@lunch_scraper_3.route('/index.html')
@lunch_scraper_3.route('/home.html')
def index_route():
    """City names and descriptions"""
    return render_template('home.html', card_data=data_dict())


@lunch_scraper_3.route('/<string:city>')
def city_route(city):
    city = get_data_for_(city)
    return render_template('city.html', city=city)


@lunch_scraper_3.route('/<string:city>/<string:district>')
def district_route(city, district):
    city = get_data_for_(city)
    district = [_ for _ in city.districts if _.name == district][0]
    return render_template('district.html',
                           city=city,
                           district=district)


@lunch_scraper_3.route('/<string:city>/<string:district>/<string:restaurant>')
def restaurant_route(city, district, restaurant):
    city = get_data_for_(city)
    district = [_ for _ in city.districts if _.name == district][0]
    restaurant = [_ for _ in district.restaurants if _.name == restaurant][0]
    return render_template('restaurant.html',
                           city=city,
                           district=district,
                           restaurant=restaurant)


if __name__ == '__main__':
    lunch_scraper_3.run(debug=True)
