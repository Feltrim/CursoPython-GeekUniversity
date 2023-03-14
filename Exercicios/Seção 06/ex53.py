n = int(input("Digite o número de linhas do Triângulo de Floyd: "))
numero = 1
for i in range(n):
    for j in range(i + 1):
        print(numero, end=" ")
        numero += 1
    print()
