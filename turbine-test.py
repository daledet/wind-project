import os
import requests
import getters
import helpers
os.system('clear')


class Turbine:
    def __init__(self, location, sweep_radius, coefficient_of_performance):
        self.location = location
        self.sweep_radius = sweep_radius
        self.coefficient_of_performance = coefficient_of_performance

    def power_output(self, wind_speed, sweep_radius, coefficient_of_performance=0.4):
        # P = 0.5Apv^3(COP)
        return (0.5 * sweep_radius * 1.2 * wind_speed ** 3) * coefficient_of_performance


stavanger_turbine = Turbine('stavanger', 15, 0.4)
print(stavanger_turbine.power_output(
    getters.wind_speed_stavanger, stavanger_turbine.sweep_radius))
