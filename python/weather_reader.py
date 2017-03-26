import json
import requests

my_apikey = 'f43934a981fc48f5926e5929d3ee0760'

def getForecastAtLocation(latitude, longitude):
    url = "https://api.weather.com/v1/geocode/{0}/{1}/forecast/hourly/24hour.json?language=en-US&units=e&apiKey={2}".format(str(latitude), str(longitude), my_apikey)

    return requests.get(url).json()

def build_weather_df(lat, lon):
    weather_json = getForecastAtLocation(lat, lon)
    weather_json['forecasts'] = weather_json['forecasts'][0]
    weather_df = pd.io.json.json_normalize(weather_json)
    return weather_df
