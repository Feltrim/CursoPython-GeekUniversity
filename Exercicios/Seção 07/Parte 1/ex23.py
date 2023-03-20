conjunto1 = []
conjunto2 = []

print("Digite os valores do conjunto 1:")
for i in range(5):
    valor = float(input())
    conjunto1.append(valor)

print("Digite os valores do conjunto 2:")
for i in range(5):
    valor = float(input())
    conjunto2.append(valor)

produto_escalar = 0
for i in range(5):
    produto_escalar += conjunto1[i] * conjunto2[i]

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
print("Produto escalar:", produto_escalar)
