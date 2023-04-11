nome_arquivo = input("Digite o nome do arquivo: ")

with open(nome_arquivo, 'r') as arquivo:
    maior_nota = 0
    nome_maior_nota = ""

    for linha in arquivo:
        nome, nota = linha.split("NOME: ")[1].split(" NOTA: ")
        nota = float(nota)

        if nota > maior_nota:
            maior_nota = nota
            nome_maior_nota = nome

    print(f"Aluno com a maior nota: {nome_maior_nota}, Nota: {maior_nota}")
