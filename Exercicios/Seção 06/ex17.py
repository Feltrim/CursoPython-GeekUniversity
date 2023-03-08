n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("O número deve ser positivo!")
else:
    soma = (n * (n + 1)) // 2
    print(f"A soma dos {n} primeiros números naturais é {soma}.")
