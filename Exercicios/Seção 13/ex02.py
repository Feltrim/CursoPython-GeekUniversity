nome_arquivo = input("Digite o nome do arquivo: ")

with open(nome_arquivo, 'r') as arquivo:
    num_linhas = 0
    for linha in arquivo:
        num_linhas += 1

print(f"O arquivo {nome_arquivo} possui {num_linhas} linhas.")
