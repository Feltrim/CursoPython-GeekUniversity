numero = int(input("Digite um número inteiro maior que zero: "))
if numero <= 0:
    print("Número inválido")
else:
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    print("A soma dos algarismos é:", soma)
