def media(vetor):
    soma = 0
    n = len(vetor)
    for i in range(n):
        soma += vetor[i]
    return soma / n
