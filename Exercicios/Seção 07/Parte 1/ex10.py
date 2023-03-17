notas = []
for i in range(15):
    nota = float(input("Digite a nota do aluno {}: ".format(i+1)))
    notas.append(nota)

media = sum(notas) / len(notas)

print("A média geral das notas de prova é: {:.2f}".format(media))
