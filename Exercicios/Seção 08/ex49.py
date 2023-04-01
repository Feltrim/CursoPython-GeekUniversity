def soma_abaixo_diagonal(matriz):
    soma = 0
    for i in range(1, len(matriz)):
        for j in range(i):
            soma += matriz[i][j]
    return soma
