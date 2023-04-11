with open('entrada.txt', 'r') as arquivo_entrada:
    linha, coluna = map(int, arquivo_entrada.readline().split())
    n = int(arquivo_entrada.readline())
    posicoes = []
    for i in range(n):
        posicoes.append(tuple(map(int, arquivo_entrada.readline().split())))

matriz = [[1] * coluna for _ in range(linha)]

for i, j in posicoes:
    matriz[i][j] = 0

with open('saida.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'{linha} {coluna}\n')
    for linha_matriz in matriz:
        linha_matriz_str = ' '.join(map(str, linha_matriz))
        arquivo_saida.write(f'{linha_matriz_str}\n')
