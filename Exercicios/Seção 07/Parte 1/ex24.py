
mais_baixo = [0, 100]
mais_alto = [0, 0]

for i in range(1, 11):
    numero_aluno = int(input(f"Digite o número do {i}º aluno: "))
    altura_aluno = float(
        input(f"Digite a altura do {i}º aluno (em metros): "))

    if altura_aluno < mais_baixo[1]:
        mais_baixo = [numero_aluno, altura_aluno]

    if altura_aluno > mais_alto[1]:
        mais_alto = [numero_aluno, altura_aluno]

print(
    f"O aluno mais baixo é o número {mais_baixo[0]}, com {mais_baixo[1]} metros de altura.")
print(
    f"O aluno mais alto é o número {mais_alto[0]}, com {mais_alto[1]} metros de altura.")
