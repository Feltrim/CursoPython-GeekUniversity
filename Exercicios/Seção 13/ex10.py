arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
arquivo_saida = input("Digite o nome do arquivo de saída: ")

with open(arquivo_entrada, "r") as f:
    linha = f.readline()
    cidade_populosa, populacao = linha[:40], int(linha[40:])

    for linha in f:
        cidade, habitantes = linha[:40], int(linha[40:])
        if habitantes > populacao:
            cidade_populosa, populacao = cidade, habitantes

with open(arquivo_saida, "w") as f:
    f.write(f"{cidade_populosa.strip()} {populacao}")
