
import sys
from collections import namedtuple
import requests

Weather = namedtuple('Weather', ['location_name', 'the_temp', 'air_pressure', 'humidity'])
def get_location_id(location_name):

    pass

def get_location_weather(location_id):
    pass

def weather_report(weather):
    pass

location_name = sys.argv[1]
location_id = get_location_id(location_name)
weather = get_location_weather(location_id)
report = weather_report(weather)
print(report)


# url = "https://www.metaweather.com/api/location/44418/"
# resp = requests.get(url)
# print(resp.json()[0]['woeid'])


