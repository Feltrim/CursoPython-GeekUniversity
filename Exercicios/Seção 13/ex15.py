ano_atual = int(input("Digite o ano corrente: "))

nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

arquivo_entrada = open(nome_arquivo_entrada, "r")
arquivo_saida = open(nome_arquivo_saida, "w")

for linha in arquivo_entrada:
    nome, ano_nascimento = linha.strip().split(",")

    idade = ano_atual - int(ano_nascimento)

    if idade < 18:
        arquivo_saida.write(f"{nome}: menor de idade\n")
    elif idade > 18:
        arquivo_saida.write(f"{nome}: maior de idade\n")
    else:
        arquivo_saida.write(f"{nome}: entrando na maior idade\n")

arquivo_entrada.close()
arquivo_saida.close()
