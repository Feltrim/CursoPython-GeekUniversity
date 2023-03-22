n = int(input("Digite um número inteiro positivo: "))

triangulo = [[1], [1, 1]]

for i in range(2, n):
    linha = [1]
    for j in range(1, i):
        linha.append(triangulo[i-1][j-1] + triangulo[i-1][j])
    linha.append(1)
    triangulo.append(linha)

for linha in triangulo:
    for numero in linha:
        print(numero, end=' ')
    print()
