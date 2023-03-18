vetor = []
for i in range(10):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    vetor.append(valor)

for i in range(10):
    if vetor[i] < 0:
        vetor[i] = 0

print("Vetor resultante:")
print(vetor)
