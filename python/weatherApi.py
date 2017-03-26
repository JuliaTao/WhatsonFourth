import requests

my_apikey = 'f43934a981fc48f5926e5929d3ee0760'

lat = 47.5946690
lon = -122.3050470

def getForecastAtLocation(latitude, longitude):
    url = "https://api.weather.com/v1/geocode/{0}/{1}/forecast/hourly/24hour.json?language=en-US&units=e&apiKey={2}".format(str(latitude), str(longitude), my_apikey)

    return requests.get(url).json()

from pprint import pprint
pprint(getForecastAtLocation(lat, lon))
