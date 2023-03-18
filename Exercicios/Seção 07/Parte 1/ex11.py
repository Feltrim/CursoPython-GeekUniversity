vetor = []

for i in range(10):
    numero = float(input("Digite um número real: "))
    vetor.append(numero)

quantidade_negativos = 0
soma_positivos = 0
for numero in vetor:
    if numero < 0:
        quantidade_negativos += 1
    else:
        soma_positivos += numero

print("Quantidade de números negativos: ", quantidade_negativos)
print("Soma dos números positivos: ", soma_positivos)
