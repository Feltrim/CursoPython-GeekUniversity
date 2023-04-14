def main():
    turma = {}

    while True:
        print("Escolha uma das opções:")
        print("(a) Definir informações da turma")
        print("(b) Inserir aluno e notas")
        print("(c) Exibir alunos e médias")
        print("(d) Exibir alunos aprovados")
        print("(e) Exibir alunos reprovados")
        print("(f) Salvar dados em Disco")
        print("(g) Sair do programa")

        opcao = input("> ")

        if opcao == 'a':
            turma = definir_turma()
        elif opcao == 'b':
            inserir_aluno(turma)
        elif opcao == 'c':
            exibir_medias(turma)
        elif opcao == 'd':
            exibir_aprovados(turma)
        elif opcao == 'e':
            exibir_reprovados(turma)
        elif opcao == 'f':
            salvar_dados(turma)
        elif opcao == 'g':
            break
        else:
            print("Opção inválida. Tente novamente.")


def definir_turma():
    turma = {}

    turma['nome'] = input("Nome da turma: ")
    turma['disciplina'] = input("Nome da disciplina: ")
    turma['professor'] = input("Nome do professor: ")

    return turma


def inserir_aluno(turma):
    nome = input("Nome do aluno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    turma[nome] = notas


def exibir_medias(turma):
    for nome, notas in turma.items():
        media = sum(notas)/len(notas)
        print(f"{nome}: {media:.2f}")


def exibir_aprovados(turma):
    for nome, notas in turma.items():
        media = sum(notas)/len(notas)
        if media >= 7:
            print(f"{nome}: {media:.2f}")


def exibir_reprovados(turma):
    for nome, notas in turma.items():
        media = sum(notas)/len(notas)
        if media < 7:
            print(f"{nome}: {media:.2f}")


def salvar_dados(turma):
    with open('notas.txt', 'w') as arquivo:
        arquivo.write(f"Turma: {turma['nome']}\n")
        arquivo.write(f"Disciplina: {turma['disciplina']}\n")
        arquivo.write(f"Professor: {turma['professor']}\n\n")
        arquivo.write("Alunos e notas:\n\n")
        for nome, notas in turma.items():
            arquivo.write(f"{nome}: ")
            arquivo.write(", ".join(str(n) for n in notas))
            arquivo.write("\n")

    print("Dados salvos com sucesso.")


if __name__ == '__main__':
    main()
