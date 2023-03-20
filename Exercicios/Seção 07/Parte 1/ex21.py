A = []
B = []

print("Informe os valores do vetor A:")
for i in range(10):
    valor = int(input(f"Valor {i+1}: "))
    A.append(valor)

print("\nInforme os valores do vetor B:")
for i in range(10):
    valor = int(input(f"Valor {i+1}: "))
    B.append(valor)

C = []
for i in range(10):
    C.append(A[i] - B[i])

print("\nVetor C:")
for valor in C:
    print(valor)
