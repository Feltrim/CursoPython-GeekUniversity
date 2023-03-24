A = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(num)
    A.append(linha)

B = []
for i in range(3):
    linha = []
    for j in range(3):
        soma = 0
        for k in range(3):
            soma += A[i][k] * A[k][j]
        linha.append(soma)
    B.append(linha)

print('Matriz A:')
for i in range(3):
    for j in range(3):
        print(A[i][j], end=' ')
    print()
print('Matriz B:')
for i in range(3):
    for j in range(3):
        print(B[i][j], end=' ')
    print()
