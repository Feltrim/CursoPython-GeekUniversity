vetor1 = []
vetor2 = []

print("Digite os elementos do primeiro vetor:")
for i in range(10):
    elemento = int(input())
    vetor1.append(elemento)

print("Digite os elementos do segundo vetor:")
for i in range(10):
    elemento = int(input())
    vetor2.append(elemento)

conjunto_uniao = set(vetor1) | set(vetor2)

vetor_uniao = sorted(list(conjunto_uniao))

print("Vetor união:", vetor_uniao)
