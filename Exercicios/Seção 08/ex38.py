def fatorial_exponencial(n):
    fatorial = 1
    for i in range(2, n+1):
        fatorial *= i
    return fatorial ** n
