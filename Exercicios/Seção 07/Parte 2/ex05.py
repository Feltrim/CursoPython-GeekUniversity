matriz = []
for i in range(5):
    linha = input(f"Digite os valores da linha {i+1}, separados por espaço: ")
    valores = linha.split()
    valores = [int(v) for v in valores]
    matriz.append(valores)

x = int(input("Digite o valor a ser buscado: "))

encontrado = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == x:
            print(f"O valor {x} foi encontrado na linha {i+1} e coluna {j+1}")
            encontrado = True

if not encontrado:
    print("O valor não foi encontrado na matriz.")
