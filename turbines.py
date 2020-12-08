import os
import requests
import getters
import helpers
os.system('clear')


class Turbine:
    def __init__(self, location, sweep):
        self.location = location
        self.sweep = sweep


class WindSpeed:
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction


turbine_stavanger = Turbine("stavanger", 5)
wind_speed_stavanger = WindSpeed(
    getters.wind_speed_stavanger, getters.wind_degree_stavanger)


helpers.turbine_status(getters.wind_speed_stavanger)
helpers.power_output(5, getters.wind_speed_stavanger)
