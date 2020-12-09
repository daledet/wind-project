import os
import requests
import getters
import helpers
os.system('clear')


class Turbine:
    def __init__(self, location):
        self.location = location


class WindSpeed:
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction


# turbine_stavanger = Turbine(getters.turbine_location)

wind_speed_stavanger = WindSpeed(
    getters.wind_speed_stavanger, getters.wind_degree_stavanger)

print(f'Wind Speed: {getters.wind_speed_stavanger}')
print(f'Status: {helpers.turbine_status(getters.wind_speed_stavanger)}')
print(f'kW: {helpers.power_output(15, getters.wind_speed_stavanger)}')
