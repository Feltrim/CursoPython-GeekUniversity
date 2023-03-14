a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
soma = 0

for num in range(a, b+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            soma += num

print(f"A soma dos números primos entre {a} e {b} é {soma}")
