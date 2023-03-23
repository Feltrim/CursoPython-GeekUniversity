import random

matriz = [[random.randint(1, 20) for j in range(4)] for i in range(4)]

print("Matriz original:")
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end="\t")
    print()

for i in range(4):
    for j in range(i+1, 4):
        matriz[i][j] = 0

print("\nMatriz triangular inferior:")
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end="\t")
    print()
