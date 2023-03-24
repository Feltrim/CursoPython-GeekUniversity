matriz1 = []
matriz2 = []

print("Digite os elementos da primeira matriz 2x2:")
for i in range(2):
    linha = []
    for j in range(2):
        elemento = float(input(f"Elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz1.append(linha)

print("\nDigite os elementos da segunda matriz 2x2:")
for i in range(2):
    linha = []
    for j in range(2):
        elemento = float(input(f"Elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz2.append(linha)

opcao = 0
while opcao != 4:
    print("\nMENU DE OPÇÕES:")
    print("1 - Somar as duas matrizes")
    print("2 - Subtrair a primeira matriz da segunda")
    print("3 - Adicionar uma constante às duas matrizes")
    print("4 - Imprimir as matrizes")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        matriz3 = []
        for i in range(2):
            linha = []
            for j in range(2):
                elemento = matriz1[i][j] + matriz2[i][j]
                linha.append(elemento)
            matriz3.append(linha)
        print("\nResultado da soma das duas matrizes:")
        for i in range(2):
            for j in range(2):
                print(matriz3[i][j], end=" ")
            print()

    elif opcao == 2:
        matriz3 = []
        for i in range(2):
            linha = []
            for j in range(2):
                elemento = matriz2[i][j] - matriz1[i][j]
                linha.append(elemento)
            matriz3.append(linha)
        print("\nResultado da subtração da primeira matriz da segunda:")
        for i in range(2):
            for j in range(2):
                print(matriz3[i][j], end=" ")
            print()

    elif opcao == 3:
        constante = float(input("Digite a constante a ser adicionada: "))
        for i in range(2):
            for j in range(2):
                matriz1[i][j] += constante
                matriz2[i][j] += constante
        print(f"\nMatriz 1 com a constante adicionada:\n{matriz1}")
        print(f"\nMatriz 2 com a constante adicionada:\n{matriz2}")

    elif opcao == 4:
        print("\nMatriz 1:")
        for i in range(2):
            for j in range(2):
                print(matriz1[i][j], end=" ")
            print()

        print("\nMatriz 2:")
        for i in range(2):
            for j in range(2):
                print(matriz2[i][j], end=" ")
            print()

    else:
        print("Opção inválida. Escolha novamente.")
