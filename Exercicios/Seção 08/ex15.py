def forma_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def tipo_triangulo(a, b, c):
    if a == b and b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if forma_triangulo(a, b, c):
    print("Os lados formam um triângulo", tipo_triangulo(a, b, c))
else:
    print("Os lados não formam um triângulo.")
