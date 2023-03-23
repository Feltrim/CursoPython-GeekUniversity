matriz = []
for i in range(3):
    linha = []
    for j in range(6):
        elemento = float(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

soma_colunas_impares = 0
for j in range(1, 6, 2):
    for i in range(3):
        soma_colunas_impares += matriz[i][j]
print(f"A soma dos elementos das colunas ímpares é {soma_colunas_impares}")

soma_colunas_2_e_4 = 0
for i in range(3):
    soma_colunas_2_e_4 += matriz[i][1] + matriz[i][3]
media_colunas_2_e_4 = soma_colunas_2_e_4 / 6
print(
    f"A média aritmética dos elementos das colunas 2 e 4 é {media_colunas_2_e_4}")

for i in range(3):
    matriz[i][5] = matriz[i][0] + matriz[i][1]

print("Matriz modificada:")
for i in range(3):
    for j in range(6):
        print(matriz[i][j], end=" ")
    print()
