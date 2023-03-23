respostas = []
for i in range(5):
    linha = []
    for j in range(10):
        resposta = input(f"Digite a resposta da questão {j+1} do aluno {i+1}: ")
        linha.append(resposta)
    respostas.append(linha)

gabarito = []
for i in range(10):
    resposta = input(f"Digite a resposta da questão {i+1} do gabarito: ")
    gabarito.append(resposta)

pontuacoes = []
for i in range(5):
    pontuacao = 0
    for j in range(10):
        if respostas[i][j] == gabarito[j]:
            pontuacao += 1
    pontuacoes.append(pontuacao)

print("Pontuações dos alunos:")
for i in range(5):
    print(f"Aluno {i+1}: {pontuacoes[i]}")
