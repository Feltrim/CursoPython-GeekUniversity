def superfatorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        fatorial = 1
        for j in range(1, i + 1):
            fatorial *= j
        result *= fatorial

    return result
