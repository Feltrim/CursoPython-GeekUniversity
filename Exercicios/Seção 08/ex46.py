def imprimir_vetor(v):
    for i in range(len(v)):
        print(v[i], end=' ')
    print()


def imprimir_vetor_inverso(v):
    for i in range(len(v)-1, -1, -1):
        print(v[i], end=' ')
    print()


def calcular_media(v):
    soma = 0
    for i in range(len(v)):
        soma += v[i]
    media = soma / len(v)
    return media
