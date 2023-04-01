def conta_maiores_que_10(matriz):
    qtd_maiores_que_10 = 0
    for linha in matriz:
        for elemento in linha:
            if elemento > 10:
                qtd_maiores_que_10 += 1
    return qtd_maiores_que_10
