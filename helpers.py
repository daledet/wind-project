import getters
import requests
import math


def turbine_status(wind_speed):
    if wind_speed < 3:
        return "Off"
    if wind_speed >= 3:
        return "On"


# Need to add cutin / cutout speed
def power_output(sweep, wind_speed, coefficient_of_performance=0.4):
    # P = 0.5Apv^3
    return (0.5 * sweep * 1.2 * wind_speed ** 3) * coefficient_of_performance
