notas = []
pior_nota_prova1 = pior_nota_prova2 = pior_nota_prova3 = 0

for i in range(10):
    notas.append([])
    for j in range(3):
        notas[i].append(float(input(f"Nota do aluno {i+1} na prova {j+1}: ")))

for i in range(10):
    pior_nota = min(notas[i])
    if pior_nota == notas[i][0]:
        pior_nota_prova1 += 1
    elif pior_nota == notas[i][1]:
        pior_nota_prova2 += 1
    else:
        pior_nota_prova3 += 1

print(f"Quantidade de alunos com pior nota na prova 1: {pior_nota_prova1}")
print(f"Quantidade de alunos com pior nota na prova 2: {pior_nota_prova2}")
print(f"Quantidade de alunos com pior nota na prova 3: {pior_nota_prova3}")
