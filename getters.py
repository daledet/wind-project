import requests
import json
import os
import datetime
os.system('clear')


response = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?id=3137115&appid=4fbcfd9147ff6df0e3ee3de039a4e70c&units=metric")

wind_speed_stavanger = response.json()['wind']['speed']
wind_degree_stavanger = response.json()['wind']['deg']
turbine_location = response.json()['name']

print(wind_speed_stavanger)

# print("----------------")

data = response.json()
print(data)

# print("----------------")

# sunrise = response.json()['sys']['sunrise']
# print(sunrise)

# ts_epoch = sunrise
# ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%H:%M:%S')
# print(ts)
