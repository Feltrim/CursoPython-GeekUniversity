matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    soma += matriz[i][i]

print("\nMatriz:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()
print(f"Soma dos elementos da diagonal principal: {soma}")
