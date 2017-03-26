import pandas as pd
from weatherApi import getDrivingDistance

def main(my_lat, my_lon):
    my_location = (my_lat, my_lon)
    hikes = loadHikes()
    print(getHikeDistances(my_location, hikes))

def getHikeDistances(current_loc, hike_df):
    hike_df.apply(lambda row: getDrivingDistance(row['lat'], row['long']) )

def loadHikes():
    return pd.read_csv('./data/washington_hikes-pp001-015.csv')


lat = 47.5946690
lon = -122.3050470
main(lat, lon)
