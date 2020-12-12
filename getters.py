import requests
import json
import config
import os
import datetime
os.system('clear')


url = "http://api.openweathermap.org/data/2.5/weather?id=3137115&"

response = requests.get(url, config.api)
data = response.json()
# print(data)

# print("----------------")


wind_speed_stavanger = response.json()['wind']['speed']
wind_degree_stavanger = response.json()['wind']['deg']
turbine_location = response.json()['name']

print(wind_speed_stavanger)


sunrise = response.json()['sys']['sunrise']
print(sunrise)

ts_epoch = sunrise
ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%H:%M:%S')
print(ts)
