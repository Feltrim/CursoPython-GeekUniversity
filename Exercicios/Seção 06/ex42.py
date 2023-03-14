import math

while True:
    valor = float(input("Digite um valor (digite 0 ou negativo para sair): "))
    if valor <= 0:
        break
    print(f"Quadrado: {valor ** 2}")
    print(f"Cubo: {valor ** 3}")
    print(f"Raiz quadrada: {math.sqrt(valor)}")
