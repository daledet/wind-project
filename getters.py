import requests
import json
import config
import os
import datetime
os.system('clear')


url_stavanger = "http://api.openweathermap.org/data/2.5/weather?id=3137115&"
url_bergen = "http://api.openweathermap.org/data/2.5/weather?id=3161733&"

response_stavanger = requests.get(url_stavanger, config.api)
response_bergen = requests.get(url_bergen, config.api)

data_stavanger = response_stavanger.json()
data_bergen = response_bergen.json()

print(data_stavanger)
print(data_bergen)

# print("----------------")


wind_speed_stavanger = response_stavanger.json()['wind']['speed']
wind_degree_stavanger = response_stavanger.json()['wind']['deg']
turbine_location_stavanger = response_stavanger.json()['name']

wind_speed_bergen = response_bergen.json()['wind']['speed']
wind_degree_bergen = response_bergen.json()['wind']['deg']
turbine_location_bergen = response_bergen.json()['name']

print(wind_speed_stavanger)
print(wind_speed_bergen)


# sunrise = response.json()['sys']['sunrise']
# print(sunrise)

# ts_epoch = sunrise
# ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%H:%M:%S')
# print(ts)
