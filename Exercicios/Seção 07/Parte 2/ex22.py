print("Matriz A")
A = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor para A[{i+1}][{j+1}]: "))
        linha.append(valor)
    A.append(linha)

print("Matriz B")
B = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor para B[{i+1}][{j+1}]: "))
        linha.append(valor)
    B.append(linha)

C = []
for i in range(3):
    linha = []
    for j in range(3):
        soma = 0
        for k in range(3):
            soma += A[i][k] * B[k][j]
        linha.append(soma)
    C.append(linha)

print("Matriz C = A * B")
for i in range(3):
    for j in range(3):
        print(C[i][j], end=" ")
    print()
