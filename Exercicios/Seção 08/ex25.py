def calcular_serie(n):
    soma = 0
    for i in range(2, n+1):
        soma += (i**2 + 1)/(i + 3)
    return soma


n = int(input("Digite o valor de N: "))
resultado = calcular_serie(n)
print("O resultado da série é:", resultado)
