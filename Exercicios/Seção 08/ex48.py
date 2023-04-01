def soma_acima_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            soma += matriz[i][j]
    return soma
