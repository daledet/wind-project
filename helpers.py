def turbine_status(wind_speed):
    if wind_speed < 5:
        print("Off")
    if wind_speed >= 5:
        print("On")


def power_output(sweep, wind_speed):  # Need to add cutin / cutout speed
    print(0.5 * 1.225 * sweep * wind_speed ** 3)
