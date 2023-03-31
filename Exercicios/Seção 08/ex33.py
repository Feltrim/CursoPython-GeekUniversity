def soma_digitos_fatorial(N):
    fatorial = 1
    for i in range(1, N+1):
        fatorial *= i

    soma = 0
    for d in str(fatorial):
        soma += int(d)

    return soma
