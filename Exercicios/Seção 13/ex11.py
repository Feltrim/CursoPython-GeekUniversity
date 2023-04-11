nome_arquivo = input("Digite o nome do arquivo: ")
palavra = input("Digite a palavra a ser procurada: ")

with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

num_ocorrencias = conteudo.count(palavra)

print(f"A palavra '{palavra}' aparece {num_ocorrencias} vezes no arquivo.")
