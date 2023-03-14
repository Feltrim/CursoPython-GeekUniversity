while True:
    print("Selecione a opção:")
    print("1 - Converter km/h para m/s")
    print("2 - Converter m/s para km/h")
    print("0 - Finalizar o programa")
    opcao = int(input("Opção: "))

    if opcao == 0:
        break

    elif opcao == 1:
        kmh = float(input("Informe a velocidade em km/h: "))
        ms = kmh / 3.6
        print("Velocidade em m/s: {:.2f}".format(ms))

    elif opcao == 2:
        ms = float(input("Informe a velocidade em m/s: "))
        kmh = ms * 3.6
        print("Velocidade em km/h: {:.2f}".format(kmh))

    else:
        print("Opção inválida. Tente novamente.")
