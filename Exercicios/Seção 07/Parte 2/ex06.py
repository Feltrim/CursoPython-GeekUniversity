# criando as duas matrizes
import random
matriz1 = [[0] * 4 for i in range(4)]
matriz2 = [[0] * 4 for i in range(4)]

# preenchendo as matrizes com valores aleatórios entre 0 e 99
for i in range(4):
    for j in range(4):
        matriz1[i][j] = random.randint(0, 99)
        matriz2[i][j] = random.randint(0, 99)

matriz_resultado = [[0] * 4 for i in range(4)]
for i in range(4):
    for j in range(4):
        matriz_resultado[i][j] = max(matriz1[i][j], matriz2[i][j])

print("Matriz 1:")
for i in range(4):
    for j in range(4):
        print(matriz1[i][j], end=" ")
    print()
print()

print("Matriz 2:")
for i in range(4):
    for j in range(4):
        print(matriz2[i][j], end=" ")
    print()
print()

print("Matriz resultado:")
for i in range(4):
    for j in range(4):
        print(matriz_resultado[i][j], end=" ")
    print()
