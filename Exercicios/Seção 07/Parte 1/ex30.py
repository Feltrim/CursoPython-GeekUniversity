vetor1 = []
vetor2 = []

print("Digite os elementos do primeiro vetor:")
for i in range(10):
    num = int(input())
    vetor1.append(num)

print("Digite os elementos do segundo vetor:")
for i in range(10):
    num = int(input())
    vetor2.append(num)

vetor_interseccao = []
for num in vetor1:
    if num in vetor2 and num not in vetor_interseccao:
        vetor_interseccao.append(num)

print("Os elementos em comum entre os dois vetores são:", vetor_interseccao)
