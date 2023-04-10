nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

    vogais = ['a', 'e', 'i', 'o', 'u']

    num_vogais = 0

    for caractere in conteudo:
        if caractere.lower() in vogais:
            num_vogais += 1

    print("O arquivo tem", num_vogais, "vogais.")
