tabuleiro = [[-1, 1, 1],
             [-1, -1, 0],
             [0, 1, 0]]

for i in range(3):
    if tabuleiro[i].count(-1) == 2 and tabuleiro[i].count(0) == 1:
        j = tabuleiro[i].index(0)
        tabuleiro[i][j] = -1
        print("Jogada recomendada: linha", i, "coluna", j)
        break

if j is None:
    for j in range(3):
        coluna = [tabuleiro[i][j] for i in range(3)]
        if coluna.count(-1) == 2 and coluna.count(0) == 1:
            i = coluna.index(0)
            tabuleiro[i][j] = -1
            print("Jogada recomendada: linha", i, "coluna", j)
            break

if j is None:
    diagonal1 = [tabuleiro[i][i] for i in range(3)]
    if diagonal1.count(-1) == 2 and diagonal1.count(0) == 1:
        i = diagonal1.index(0)
        tabuleiro[i][i] = -1
        print("Jogada recomendada: linha", i, "coluna", i)
    else:
        diagonal2 = [tabuleiro[i][2-i] for i in range(3)]
        if diagonal2.count(-1) == 2 and diagonal2.count(0) == 1:
            i = diagonal2.index(0)
            tabuleiro[i][2-i] = -1
            print("Jogada recomendada: linha", i, "coluna", 2-i)
        else:
            print("Não há jogadas recomendadas")
