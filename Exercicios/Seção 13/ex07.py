nome_arquivo = input("Digite o nome do arquivo de entrada: ")

with open(nome_arquivo, "r") as arq_entrada:
    conteudo = arq_entrada.read()

vogais = "aeiouAEIOU"
novo_conteudo = ""
for letra in conteudo:
    if letra in vogais:
        novo_conteudo += "*"
    else:
        novo_conteudo += letra

nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

with open(nome_arquivo_saida, "w") as arq_saida:
    arq_saida.write(novo_conteudo)

print("Arquivo criado com sucesso!")
