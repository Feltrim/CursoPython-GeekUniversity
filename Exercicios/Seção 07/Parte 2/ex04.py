matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

maior_valor = matriz[0][0]
maior_linha = 0
maior_coluna = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            maior_linha = i
            maior_coluna = j

print(
    f"O maior valor é {maior_valor} e está localizado na linha {maior_linha} e coluna {maior_coluna}.")
