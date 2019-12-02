import math


def fuel_calc(mass):
    fuel = (math.floor(mass / 3)) - 2
    if fuel <= 0:
        return 0

    return fuel + fuel_calc(fuel)
