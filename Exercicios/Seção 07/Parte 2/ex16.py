gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']

alunos = [
    {'matricula': 1, 'respostas': [
        'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']},
    {'matricula': 2, 'respostas': [
        'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']},
    {'matricula': 3, 'respostas': [
        'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']}
]

for aluno in alunos:
    nota = 0
    for i in range(10):
        if aluno['respostas'][i] == gabarito[i]:
            nota += 1
    aluno['nota'] = nota

for aluno in alunos:
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Respostas: {aluno['respostas']}")
    print(f"Nota: {aluno['nota']}")
    print()

total_aprovados = 0
for aluno in alunos:
    if aluno['nota'] >= 7:
        total_aprovados += 1
percentual_aprovados = (total_aprovados / len(alunos)) * 100

print(f"Percentual de aprovação: {percentual_aprovados}%")
