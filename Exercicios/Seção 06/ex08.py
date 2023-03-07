menor = maior = int(input("Digite o 1º número: "))

for i in range(2, 11):
    numero = int(input(f"Digite o {i}º número: "))
    if numero > 0:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

print(f"Menor valor lido: {menor}")
print(f"Maior valor lido: {maior}")
