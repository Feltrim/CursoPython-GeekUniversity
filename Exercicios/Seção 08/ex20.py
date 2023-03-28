def fatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial


numero = int(input("Digite um número inteiro positivo: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
