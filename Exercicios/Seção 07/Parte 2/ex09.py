matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(
            input(f"Digite o valor para a posição [{i}][{j}]: "))

soma = 0
for i in range(3):
    for j in range(i):
        soma += matriz[i][j]

print("A soma dos elementos abaixo da diagonal principal é:", soma)
