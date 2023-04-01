import math


def desvio_padrao(v):
    n = len(v)
    m = sum(v) / n
    soma_quadrados = sum((x - m)**2 for x in v)
    return math.sqrt(soma_quadrados / (n-1))
