import requests
from pysyge import GeoLocator


def get_city_name(ip):
    geodata = GeoLocator('SxGeoCity.dat')
    location = geodata.get_location(ip)
    return str(location['info']['city']['name_en'])


    # try:
    #     location = geodata.get_location(ip)
    #     return str(location['info']['city']['name_en'])
    # except TypeError:
    #     if ip == '127.0.0.1':
    #         location = geodata.get_location('8.8.8.8')
    #         return str(location['info']['city']['name_en'])
    #     else:
    #         return


def get_weather_in_city(q):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': q, 'units': 'metric', 'APPID': 'eacfa88812fdd95eea20aa01fa07d56b'}
    x = requests.get(url, params=parameters)
    return int(x.json()['main']['temp'])
