import random

def preenche_vetor_aleatorio(tamanho):
    numeros_aleatorios = set()
    while len(numeros_aleatorios) < tamanho:
        numeros_aleatorios.add(random.randint(0, 100))
    return list(numeros_aleatorios)
