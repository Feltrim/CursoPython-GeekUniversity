vetor = []
for i in range(10):
    valor = int(input("Digite um valor para a posição {}: ".format(i)))
    vetor.append(valor)

quantidade_pares = 0
for valor in vetor:
    if valor % 2 == 0:
        quantidade_pares += 1

print("O vetor possui {} valores pares.".format(quantidade_pares))
