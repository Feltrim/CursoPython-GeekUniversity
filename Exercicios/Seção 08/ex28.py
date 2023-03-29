import math


def cos_taylor(angle):
    angle = math.radians(angle)

    result = 1.0
    term = 1.0

    for n in range(1, 11):
        term *= -angle**2 / ((2*n - 1) * 2*n)

        result += term

    return result


angle = float(input("Digite o ângulo em graus: "))
cos = cos_taylor(angle)
print("O cosseno de {} graus é {:.4f}".format(angle, cos))
