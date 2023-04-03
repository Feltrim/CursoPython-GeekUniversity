def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = [[0] * linhas for _ in range(colunas)]
    for i in range(linhas):
        for j in range(colunas):
            transposta[j][i] = matriz[i][j]
    return transposta
