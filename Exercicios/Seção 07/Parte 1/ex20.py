
vetor1 = []
for i in range(10):
    num = int(input("Digite um número entre 0 e 50: "))
    while num < 0 or num > 50:
        num = int(input("Digite um número entre 0 e 50: "))
    vetor1.append(num)

vetor2 = []
for i in vetor1:
    if i % 2 != 0:
        vetor2.append(i)

print("\nVetor 1: ")
for i in range(0, 10, 2):
    print(vetor1[i], vetor1[i+1])

print("\nVetor 2: ")
for i in range(0, len(vetor2), 2):
    if i+1 < len(vetor2):
        print(vetor2[i], vetor2[i+1])
    else:
        print(vetor2[i])
