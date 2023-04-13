import struct


def cadastrar_alunos():
    n = int(input("Digite o número de alunos: "))
    alunos = []
    for i in range(n):
        nome = input("Digite o nome do aluno {}: ".format(i+1))
        nota = float(input("Digite a nota final do aluno {}: ".format(i+1)))
        alunos.append((nome[:40], nota))
    return alunos


def salvar_alunos(alunos):
    with open("alunos.bin", "wb") as arquivo:
        for aluno in alunos:
            nome_bytes = aluno[0].encode('utf-8')
            nota_bytes = struct.pack('f', aluno[1])
            arquivo.write(nome_bytes)
            arquivo.write(nota_bytes)


def ler_alunos():
    alunos = []
    with open("alunos.bin", "rb") as arquivo:
        while True:
            nome_bytes = arquivo.read(40)
            if nome_bytes == b'':
                break
            nome = nome_bytes.decode('utf-8').rstrip()
            nota_bytes = arquivo.read(4)
            nota = struct.unpack('f', nota_bytes)[0]
            alunos.append((nome, nota))
    return alunos


def main():
    opcao = input(
        "Deseja cadastrar novos alunos (1) ou ler os alunos cadastrados (2)? ")
    if opcao == '1':
        alunos = cadastrar_alunos()
        salvar_alunos(alunos)
    elif opcao == '2':
        alunos = ler_alunos()
    else:
        print("Opção inválida")
        return

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado")
        return

    maior_nota = 0
    nome_maior_nota = ""
    for aluno in alunos:
        if aluno[1] > maior_nota:
            maior_nota = aluno[1]
            nome_maior_nota = aluno[0]

    print("O aluno com a maior nota é {} com nota {}".format(
        nome_maior_nota, maior_nota))


if __name__ == '__main__':
    main()
