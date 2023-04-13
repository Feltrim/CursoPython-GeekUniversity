import pickle


def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    aniversario = input("Digite o aniversário do contato (dd/mm): ")
    agenda[nome] = (telefone, aniversario)
    print("Contato adicionado com sucesso!")


def remover_contato(agenda):
    nome = input("Digite o nome do contato que deseja remover: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado na agenda.")


def pesquisar_contato(agenda):
    nome = input("Digite o nome do contato que deseja pesquisar: ")
    if nome in agenda:
        print("Nome: ", nome)
        print("Telefone: ", agenda[nome][0])
        print("Aniversário: ", agenda[nome][1])
    else:
        print("Contato não encontrado na agenda.")


def listar_contatos(agenda):
    for nome, dados in agenda.items():
        print("Nome: ", nome)
        print("Telefone: ", dados[0])
        print("Aniversário: ", dados[1])
        print("--------------------")


def listar_contatos_por_letra(agenda):
    letra = input("Digite a letra inicial dos contatos que deseja listar: ")
    for nome, dados in agenda.items():
        if nome.startswith(letra.upper()) or nome.startswith(letra.lower()):
            print("Nome: ", nome)
            print("Telefone: ", dados[0])
            print("Aniversário: ", dados[1])
            print("--------------------")


def listar_aniversariantes_do_mes(agenda):
    mes = input(
        "Digite o número do mês (ex: 01 para janeiro) para listar os aniversariantes: ")
    for nome, dados in agenda.items():
        if dados[1][3:5] == mes:
            print("Nome: ", nome)
            print("Telefone: ", dados[0])
            print("Aniversário: ", dados[1])
            print("--------------------")


def main():
    try:
        with open('agenda.bin', 'rb') as arquivo:
            agenda = pickle.load(arquivo)
    except FileNotFoundError:
        agenda = {}
    while True:
        print("Selecione uma das opções abaixo:")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Pesquisar contato")
        print("4 - Listar contatos")
        print("5 - Listar contatos por letra")
        print("6 - Listar aniversariantes do mês")
        print("0 - Sair")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            remover_contato(agenda)
        elif opcao == '3':
            pesquisar_contato(agenda)
        elif opcao == '4':
            listar_contatos(agenda)
        elif opcao == '5':
            listar_contatos_por_letra(agenda)
        elif opcao == '6':
            listar_aniversariantes_do_mes(agenda)
        elif opcao == '0':
            with open('agenda.bin', 'wb') as arquivo:
                pickle.dump(agenda, arquivo)
            print("Agenda salva. Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite um número de 0 a 6.")
