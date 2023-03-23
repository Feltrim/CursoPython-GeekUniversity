matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

somas_colunas = []
for j in range(3):
    soma_coluna = 0
    for i in range(3):
        soma_coluna += matriz[i][j]
    somas_colunas.append(soma_coluna)

print("Array com as somas das colunas da matriz:")
print(somas_colunas)
