matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma = matriz[0][2] + matriz[1][1] + matriz[2][0]

print("Matriz:")
for linha in matriz:
    print(linha)

print("Soma dos elementos da diagonal secundária: ", soma)
