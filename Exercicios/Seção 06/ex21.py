n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma_pares = 0
mult_impares = 1

for i in range(n1, n2+1):
    if i % 2 == 0:
        soma_pares += i
    else:
        mult_impares *= i

print("A soma dos números pares é:", soma_pares)
print("A multiplicação dos números ímpares é:", mult_impares)
