quantidade = int(input("Digite a quantidade de números a serem lidos: "))

maior = None
contador_maior = 0

for i in range(quantidade):
    numero = float(input("Digite um número: "))

    if maior is None or numero > maior:
        maior = numero
        contador_maior = 1
    elif numero == maior:
        contador_maior += 1

print("O maior número lido foi", maior)
print("Ele foi lido", contador_maior, "vezes.")
