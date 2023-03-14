soma = 0
quantidade = 0
maior = -float('inf')
menor = float('inf')
soma_pares = 0
quantidade_pares = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
    quantidade += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Soma: {soma}")
    print(f"Quantidade: {quantidade}")
    print(f"Média: {media}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
else:
    print("Nenhum número foi digitado.")

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f"Média dos números pares: {media_pares}")
else:
    print("Não foram digitados números pares.")
