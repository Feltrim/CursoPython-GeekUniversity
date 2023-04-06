def ler_string(tamanho):
    vetor = [''] * tamanho
    i = 0
    while i < tamanho:
        caractere = input()
        if caractere == '\n':
            break
        vetor[i] = caractere
        i += 1
    return vetor
