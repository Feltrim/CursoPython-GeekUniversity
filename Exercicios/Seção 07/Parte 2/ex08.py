matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for i in range(3):
    for j in range(i+1, 3):
        soma += matriz[i][j]

print("Matriz:")
for linha in matriz:
    print(linha)

print(f"Soma dos elementos acima da diagonal principal: {soma}")
