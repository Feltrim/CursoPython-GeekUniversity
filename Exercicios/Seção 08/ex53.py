def verifica_identidade(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True
