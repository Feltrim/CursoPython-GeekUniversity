vetor = []
for i in range(10):
    numero = float(input("Digite o {}o número: ".format(i+1)))
    vetor.append(numero)

for i in range(len(vetor)-1):
    menor = i
    for j in range(i+1, len(vetor)):
        if vetor[j] < vetor[menor]:
            menor = j
    if menor != i:
        vetor[i], vetor[menor] = vetor[menor], vetor[i]

print("Vetor ordenado:", vetor)
