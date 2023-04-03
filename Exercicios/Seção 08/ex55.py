def soma_diagonais(matriz):
    soma = 0
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                soma += matriz[i][j]
    return soma
