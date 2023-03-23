matriz = []
for i in range(3):
    linha = input().split()
    linha = [int(x) for x in linha]
    matriz.append(linha)

transposta = []
for j in range(3):
    linha_transposta = []
    for i in range(3):
        linha_transposta.append(matriz[i][j])
    transposta.append(linha_transposta)

for i in range(3):
    for j in range(3):
        print(transposta[i][j], end=" ")
    print()
