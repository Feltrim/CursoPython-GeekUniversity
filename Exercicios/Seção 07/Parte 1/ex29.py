pares = []
impares = []
soma_pares = 0

for i in range(6):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    if num % 2 == 0:
        pares.append(num)
        soma_pares += num
    else:
        impares.append(num)

print("Números pares digitados:", pares)
print("Soma dos números pares digitados:", soma_pares)
print("Números ímpares digitados:", impares)
print("Quantidade de números ímpares digitados:", len(impares))
