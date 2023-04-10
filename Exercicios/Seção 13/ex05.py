nome_arquivo = input("Digite o nome do arquivo: ")
caractere = input("Digite o caractere a ser procurado: ")

with open(nome_arquivo, "r") as arquivo:
    texto = arquivo.read()

qtd_ocorrencias = texto.count(caractere)

print(
    f"O caractere '{caractere}' aparece {qtd_ocorrencias} vezes no arquivo '{nome_arquivo}'.")
