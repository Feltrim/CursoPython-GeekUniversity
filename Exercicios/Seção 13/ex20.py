num_alunos = int(input("Digite o número de alunos: "))

nomes = [None] * num_alunos
notas = [None] * num_alunos

for i in range(num_alunos):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota final do {i+1}º aluno: "))
    nomes[i] = nome
    notas[i] = nota

with open("alunos.txt", "w") as arquivo:
    for i in range(num_alunos):
        nome_formatado = nomes[i].ljust(40)
        linha = f"{nome_formatado} {notas[i]}\n"
        arquivo.write(linha)
