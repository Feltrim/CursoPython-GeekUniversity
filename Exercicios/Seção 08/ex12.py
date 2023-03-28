def soma_algarismos(num):
    if num <= 0:
        return "Número inválido"
    else:
        soma = 0
        while num > 0:
            soma += num % 10
            num //= 10
        return soma


x = soma_algarismos(int(input("Digite um número maior que 0: ")))
print(x)
