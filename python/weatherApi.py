import requests
from datetime import datetime

my_apikey = 'f43934a981fc48f5926e5929d3ee0760'

lat = 47.5946690
lon = -122.3050470

def getForecastAtLocation(latitude, longitude):
    current_date_string = datetime.now().strftime("%Y%m%d")
    url = "https://api.weather.com/v1/geocode/{0}/{1}/forecast/hourly/24hour.json?language=en-US&units=e&apiKey={2}".format(str(latitude), str(longitude), my_apikey)
    return requests.get(url).json()

import geopy
from geopy.distance import great_circle
#TODO: replace with https://developers.google.com/maps/documentation/distance-matrix/intro
def getDrivingDistance(start_loc, end_loc):
    return great_circle(newport_ri, cleveland_oh).miles

def getDrivingTime(start_loc, end_loc):
    return getDrivingDistance(start_loc, end_loc) / 50 #assume 50 mph
