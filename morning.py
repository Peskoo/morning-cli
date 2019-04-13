import config

import click
import json
import requests


API_KEY = config.api_key


class MyWeather():
    def __init__(self, cityname):
        self.country = 'FR'
        self.cityname = cityname.capitalize()


    def api(self, id):
        url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'.format(
                id, API_KEY)
        response = requests.get(url)
        if response:
            return response.json()


    def city_id(self):
        with open('city.list.json', 'r') as f:
            datacities = json.load(f)

        city = [x for x in datacities
                if x['name'] == self.cityname and x['country'] == self.country]
        if city:
            return city[0]['id']
        else:
            return "Cette ville n'existe pas de mon côté"


@click.group()
def cli():
    pass


@cli.command()
def all():
    """Liste des villes disponibles."""
    with open('city.list.json', 'r') as f:
            datacities = json.load(f)
    user = input('Le nom de votre ville ? \n')
    cities = []
    for city in datacities:
        my_city = city['name'].lower()
        if my_city.find(user.lower()) >= 0 and city['country'] == 'FR':
            print(my_city.capitalize())


@cli.command()
@click.option('--city', '-c',
        default='Paris',
        help='Le nom de votre ville')
def morning(city):
    """La météo de votre ville, tout simplement."""
    # Init objet
    objet = MyWeather(city)
    _id = objet.city_id()
    _api = objet.api(_id)

    # Retrieve informations
    weather = _api['weather'][0]['main']
    temp = _api['main']['temp'] - 273.15

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
