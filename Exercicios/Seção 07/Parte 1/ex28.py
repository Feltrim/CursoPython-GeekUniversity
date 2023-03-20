v = []
v1 = []
v2 = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    v.append(num)

for num in v:
    if num % 2 == 0:
        v2.append(num)
    else:
        v1.append(num)

print("Valores ímpares em v1:")
for num in v1:
    print(num)

print("Valores pares em v2:")
for num in v2:
    print(num)
