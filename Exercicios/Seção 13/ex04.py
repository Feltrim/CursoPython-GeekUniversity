nome_arquivo = input("Digite o nome do arquivo: ")
vogais = "aeiouAEIOU"
cont_vogais = 0
cont_consoantes = 0

with open(nome_arquivo, "r") as arquivo:
    for caractere in arquivo.read():
        if caractere.isalpha():
            if caractere in vogais:
                cont_vogais += 1
            else:
                cont_consoantes += 1

print("O arquivo contém", cont_vogais,
      "vogais e", cont_consoantes, "consoantes.")
