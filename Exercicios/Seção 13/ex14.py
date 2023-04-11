from datetime import datetime

nome_arquivo = input("Informe o nome do arquivo com as datas de nascimento: ")

data_atual = input("Informe a data atual (DD MM AAAA): ")
dia_atual, mes_atual, ano_atual = map(int, data_atual.split())

with open(nome_arquivo, "r") as arquivo_nomes:
    with open("idades.txt", "w") as arquivo_idades:
        for linha in arquivo_nomes:
            nome, dia_nasc, mes_nasc, ano_nasc = linha.strip().split()
            data_nasc = datetime(int(ano_nasc), int(mes_nasc), int(dia_nasc))
            idade = (datetime.now() - data_nasc).days // 365
            arquivo_idades.write(f"{nome}: {idade} anos\n")

print("O arquivo com as idades foi salvo como 'idades.txt'.")
