opcao = int(input("""Escolha a opção:\n
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).\n
Opção: """))

if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("A soma é: ", num1 + num2)
elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num1 > num2:
        print("A diferença é: ", num1 - num2)
    else:
        print("A diferença é: ", num2 - num1)
elif opcao == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("O produto é: ", num1 * num2)
elif opcao == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        print("Não é possível dividir por zero.")
    else:
        print("A divisão é: ", num1 / num2)
else:
    print("Opção inválida.")
