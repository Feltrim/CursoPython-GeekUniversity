import re
from collections import Counter

nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

num_caracteres = len(conteudo)
num_linhas = len(conteudo.split("\n"))
num_palavras = len(re.findall(r"\b\w+\b", conteudo))

ocorrencias = Counter(re.findall(r"[a-zA-Z]", conteudo))

print("Número de caracteres:", num_caracteres)
print("Número de linhas:", num_linhas)
print("Número de palavras:", num_palavras)
print("Ocorrências de cada letra:")
for letra, ocorrencia in ocorrencias.items():
    print(letra, "-", ocorrencia)
