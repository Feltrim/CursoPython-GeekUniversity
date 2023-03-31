def fatorial_duplo(N):
    if N % 2 == 0:
        return None

    fatorial = 1
    for i in range(1, N + 1, 2):
        fatorial *= i

    return fatorial
