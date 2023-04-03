def soma_coluna(matriz, coluna):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][coluna]
    return soma
