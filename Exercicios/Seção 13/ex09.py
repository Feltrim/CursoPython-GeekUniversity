arq1 = input("Digite o nome do primeiro arquivo: ")
arq2 = input("Digite o nome do segundo arquivo: ")
arq_saida = input("Digite o nome do arquivo de saída: ")

with open(arq1, 'r') as f1, open(arq2, 'r') as f2, open(arq_saida, 'w') as f_saida:
    for linha in f1:
        f_saida.write(linha)
    for linha in f2:
        f_saida.write(linha)

print("Arquivos combinados com sucesso!")
