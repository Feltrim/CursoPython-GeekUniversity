def uniao_vetores(vetor1, vetor2):
    vetor_uniao = [0] * 20
    for i in range(10):
        vetor_uniao[i] = vetor1[i]
    for i in range(10):
        vetor_uniao[i+10] = vetor2[i]
    return vetor_uniao
