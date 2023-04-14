class Aluno:
    def __init__(self, matricula, sobrenome, ano_nascimento):
        self.matricula = matricula
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento


def main():
    num_alunos = int(
        input("Informe o número de alunos a serem cadastrados: "))
    alunos = []
    for i in range(num_alunos):
        print(f"Aluno {i+1}:")
        matricula = input("Matrícula: ")
        sobrenome = input("Sobrenome: ")
        ano_nascimento = int(input("Ano de nascimento: "))
        aluno = Aluno(matricula, sobrenome, ano_nascimento)
        alunos.append(aluno)
    with open('alunos.txt', 'w') as arquivo:
        for aluno in alunos:
            arquivo.write(
                f"{aluno.matricula};{aluno.sobrenome};{aluno.ano_nascimento}\n")


if __name__ == '__main__':
    main()
