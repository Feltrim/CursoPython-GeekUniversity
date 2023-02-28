import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

if a == 0:
    print("Não é equação de segundo grau")
else:
    if delta < 0:
        print("Não existe raiz real.")
    elif delta == 0:
        raiz = -b / (2*a)
        print("Raiz única:", raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print("Raízes:", raiz1, "e", raiz2)
