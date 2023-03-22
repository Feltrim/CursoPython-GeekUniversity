matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append((i+1)*(j+1))
    matriz.append(linha)

for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=' ')
    print()
