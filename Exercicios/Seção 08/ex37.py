def hiperfatorial(n):
    produto = 1
    for i in range(1, n+1):
        produto *= i**i
    return produto
