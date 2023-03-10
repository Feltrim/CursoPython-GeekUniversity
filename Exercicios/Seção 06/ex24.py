num = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, num):
    if num % i == 0:
        soma += i

print("A soma dos divisores de", num, "é:", soma)
