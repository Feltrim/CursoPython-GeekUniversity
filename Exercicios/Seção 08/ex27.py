import math


def calcular_seno():
    angulo = float(input("Digite o valor do ângulo em graus: "))

    angulo_rad = math.radians(angulo)

    seno = angulo_rad
    sinal = -1
    for i in range(1, 10, 2):
        termo = (angulo_rad ** (i+1)) / math.factorial(i+1)
        seno += sinal * termo
        sinal *= -1

    return seno


print(calcular_seno())
