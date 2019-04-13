import json
import os
import requests

import click


API_KEY = os.environ.get('API_KEY')
CITIES_DATA = None
ABSOLUTE_ZERO = 273.15
OPENWEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'


class RequestedWeather():
    def __init__(self, city_name):
        self.country = 'FR'
        self.city_name = city_name.capitalize()

    def api(self, id=None):
        if not id:
            id = self.city_id()
        url = OPENWEATHER_API_URL.format(id, API_KEY)
        response = requests.get(url)
        if response:
            return response.json()

    def city_id(self):
        city = next(x for x in CITIES_DATA
                    if x['name'] == self.city_name and x['country'] == self.country)
        if city:
            return city['id']
        else:
            click.echo("La ville {} n'existe pas de mon côté".format(self.city_name))


@click.group()
def cli():
    global CITIES_DATA
    with open('city.list.json', 'r') as f:
        CITIES_DATA = json.load(f)


@cli.command()
def all():
    """Liste des villes disponibles."""
    user = input('Le nom de votre ville ? \n')
    for city in CITIES_DATA:
        my_city = city['name'].lower()
        if my_city.find(user.lower()) >= 0 and city['country'] == 'FR':
            click.echo(my_city.capitalize())


@cli.command()
@click.option('--city', '-c',
              default='Paris',
              help='Le nom de votre ville')
def morning(city):
    """La météo de votre ville, tout simplement."""
    # Init objet
    requested_weather = RequestedWeather(city).api()

    # Retrieve informations
    weather = requested_weather['weather'][0]['main']
    temp = requested_weather['main']['temp'] - ABSOLUTE_ZERO

    # Return
    click.echo('Actuellement de votre jolie ville de {}:'.format(city))
    click.echo('------------------')
    click.echo('Temps: {}'.format(weather))
    click.echo('------------------')
    click.echo('Temperature: {}°C'.format(int(temp)))
    click.echo('------------------')
    click.echo('Bonne journée !')


if __name__ == '__main__':
    cli()
