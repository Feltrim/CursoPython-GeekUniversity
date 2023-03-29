import math


def cosh_taylor(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cosh = 1
    term = 1
    n = 2
    while True:
        term *= angle_radians**2 / (n * (n - 1))
        if term == 0:
            break
        cosh += term
        n += 2
    return cosh
