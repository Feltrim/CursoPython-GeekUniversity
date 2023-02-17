from math import sqrt

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

distancia_origem = sqrt(x**2 + y**2)

print(f"A distância da origem ({0},{0}) até o ponto ({x},{y}) é de {distancia_origem:.2f} unidades.")
