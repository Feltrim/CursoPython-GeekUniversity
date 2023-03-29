def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma


n = int(input("Digite um número inteiro positivo: "))
if n <= 0:
    print("Número inválido")
else:
    resultado = somatorio(n)
    print("O somatório de 1 até", n, "é", resultado)
