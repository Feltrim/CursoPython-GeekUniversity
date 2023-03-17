vetor = []
for i in range(10):
    valor = int(input("Digite um valor para a posição {}: ".format(i)))
    vetor.append(valor)

maior_elemento = vetor[0]
menor_elemento = vetor[0]
for valor in vetor:
    if valor > maior_elemento:
        maior_elemento = valor
    elif valor < menor_elemento:
        menor_elemento = valor

print("O maior elemento do vetor é: ", maior_elemento)
print("O menor elemento do vetor é: ", menor_elemento)
