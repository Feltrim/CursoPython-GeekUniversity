import os


def criar_arquivo():
    arquivo = input("Digite o nome do arquivo a ser criado: ")
    with open(arquivo, "w") as f:
        print("Arquivo criado com sucesso")


def imprimir_registro():
    arquivo = input("Digite o nome do arquivo: ")
    codigo = input("Digite o código do vendedor: ")
    mes = input("Digite o mês: ")
    with open(arquivo, "r") as f:
        encontrado = False
        for linha in f:
            campos = linha.strip().split(",")
            if campos[0] == codigo and campos[3] == mes:
                print(f"Código do vendedor: {campos[0]}")
                print(f"Nome verdadeiro: {campos[1]}")
                print(f"Valor da venda: {campos[2]}")
                print(f"Mês: {campos[3]}")
                encontrado = True
                break
        if not encontrado:
            print("Registro não encontrado")


def excluir_vendedor():
    arquivo = input("Digite o nome do arquivo: ")
    codigo = input("Digite o código do vendedor: ")
    mes = input("Digite o mês: ")
    with open(arquivo, "r") as f1, open("temp.txt", "w") as f2:
        excluido = False
        for linha in f1:
            campos = linha.strip().split(",")
            if campos[0] == codigo and campos[3] == mes:
                excluido = True
            else:
                f2.write(linha)
        if excluido:
            os.remove(arquivo)
            os.rename("temp.txt", arquivo)
            print("Vendedor excluído com sucesso")
        else:
            os.remove("temp.txt")
            print("Registro não encontrado")


def alterar_venda():
    arquivo = input("Digite o nome do arquivo: ")
    codigo = input("Digite o código do vendedor: ")
    mes = input("Digite o mês: ")
    novo_valor = input("Digite o novo valor da venda: ")
    with open(arquivo, "r") as f1, open("temp.txt", "w") as f2:
        alterado = False
        for linha in f1:
            campos = linha.strip().split(",")
            if campos[0] == codigo and campos[3] == mes:
                campos[2] = novo_valor
                linha = ",".join(campos) + "\n"
                alterado = True
            f2.write(linha)
        if alterado:
            os.remove(arquivo)
            os.rename("temp.txt", arquivo)
            print("Valor da venda alterado com sucesso")
        else:
            os.remove("temp.txt")
            print("Registro não encontrado")


def imprimir_registros():
    arquivo = input("Digite o nome do arquivo: ")
    with open(arquivo, "r") as f:
        for linha in f:
            campos = linha.strip().split(",")
            print(f"Código do vendedor: {campos[0]}")
            print(f"Nome verdadeiro: {campos[1]}")
            print(f"Valor da venda: {campos[2]}")
            print(f"Mês: {campos[3]}")
            print()


def excluir_arquivo():
    arquivo = input("Digite o nome do arquivo a ser excluído: ")
    if os.path.exists(arquivo):
        os.remove(arquivo)
        print(f"Arquivo {arquivo} excluído com sucesso")
    else:
        print("Arquivo não encontrado")


def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    registros = []
    fim = False
    while not fim:
        print("\nSelecione a opção desejada:")
        print("(1) Criar o arquivo de dados")
        print("(2) Imprimir um determinado registro no arquivo")
        print("(3) Excluir um determinado vendedor no arquivo")
        print("(4) Alterar o valor de uma venda no arquivo")
        print("(5) Imprimir os registros na saída padrão")
        print("(6) Excluir o arquivo de dados")
        print("(7) Finalizar o programa")
        opcao = input()
        if opcao == "1":
            registros = criar_arquivo(nome_arquivo)
            print("Arquivo criado com sucesso!")
        elif opcao == "2":
            codigo_vendedor = input("Digite o código do vendedor: ")
            mes = input("Digite o mês da venda: ")
            imprimir_registro(registros, codigo_vendedor, mes)
        elif opcao == "3":
            codigo_vendedor = input("Digite o código do vendedor: ")
            mes = input("Digite o mês da venda: ")
            registros = excluir_vendedor(registros, codigo_vendedor, mes)
            print("Vendedor excluído com sucesso!")
        elif opcao == "4":
            codigo_vendedor = input("Digite o código do vendedor: ")
            mes = input("Digite o mês da venda: ")
            valor = float(input("Digite o novo valor da venda: "))
            registros = alterar_venda(registros, codigo_vendedor, mes, valor)
            print("Valor da venda alterado com sucesso!")
        elif opcao == "5":
            imprimir_registros(registros)
        elif opcao == "6":
            excluir_arquivo(nome_arquivo)
            registros = []
            print("Arquivo excluído com sucesso!")
        elif opcao == "7":
            fim = True
            print("Programa finalizado.")
        else:
            print("Opção inválida. Digite uma opção válida.")


if __name__ == "__main__":
    main()
