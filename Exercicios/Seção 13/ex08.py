nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")

nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

try:
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        conteudo = arquivo_entrada.read()

        conteudo_modificado = conteudo.upper()

        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            arquivo_saida.write(conteudo_modificado)

        print(f"Arquivo {nome_arquivo_saida} criado com sucesso!")

except FileNotFoundError:
    print(f"Arquivo {nome_arquivo_entrada} não encontrado.")
