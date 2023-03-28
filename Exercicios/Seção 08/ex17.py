def soma_entre_numeros(a, b):
    soma = 0
    for num in range(a+1, b):
        soma += num
    return soma


a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))

soma = soma_entre_numeros(a, b)

print(f"A soma dos números inteiros entre {a} e {b} é {soma}.")
