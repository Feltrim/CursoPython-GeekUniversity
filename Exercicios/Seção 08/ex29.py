import math


def sinh_graus(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    seno_hiperbolico = 0

    for n in range(0, 50):
        numerador = math.pow(angulo_radianos, 2*n+1)
        denominador = math.factorial(2*n+1)
        seno_hiperbolico += numerador/denominador

    return seno_hiperbolico
