def soma_linha(matriz, n):
    soma = 0
    for j in range(len(matriz[0])):
        soma += matriz[n][j]
    return soma
