def contar_pares(vetor):
    cont_pares = 0
    for i in vetor:
        if i % 2 == 0:
            cont_pares += 1
    return cont_pares
