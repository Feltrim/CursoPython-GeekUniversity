while True:
    print("----- Menu de Opções -----")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 5:
        print("Saindo do programa...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = num1 + num2
        print("Resultado da adição: ", resultado)
    elif opcao == 2:
        resultado = num1 - num2
        print("Resultado da subtração: ", resultado)
    elif opcao == 3:
        resultado = num1 * num2
        print("Resultado da multiplicação: ", resultado)
    elif opcao == 4:
        if num2 == 0:
            print("Erro: divisão por zero!")
        else:
            resultado = num1 / num2
            print("Resultado da divisão: ", resultado)
    else:
        print("Opção inválida!")

    input("Pressione ENTER para continuar...")
    print()
