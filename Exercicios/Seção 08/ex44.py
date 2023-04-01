def separa_pares_impares(vetor):
    a = []
    b = []
    for i in vetor:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    return a, b
