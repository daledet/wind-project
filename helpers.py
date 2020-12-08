import getters


def turbine_status(wind_speed):
    if wind_speed < 5:
        return "Off"
    if wind_speed >= 5:
        return "On"


def power_output(sweep, wind_speed):  # Need to add cutin / cutout speed
    # 1.225 Density of air at sealevel
    if getters.wind_speed_stavanger >= 3 and getters.wind_speed_stavanger <= 12:
        return 0.5 * 1.225 * sweep * wind_speed ** 3
