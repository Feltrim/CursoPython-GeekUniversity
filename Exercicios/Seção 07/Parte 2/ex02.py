matriz = [[0 for j in range(5)] for i in range(5)]

for i in range(5):
    matriz[i][i] = 1

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()
