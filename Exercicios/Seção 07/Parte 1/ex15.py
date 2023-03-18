vetor = []
for i in range(20):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

conjunto = set(vetor)

vetor_sem_repeticao = list(conjunto)

print("Vetor sem elementos repetidos:")
for valor in vetor_sem_repeticao:
    print(valor)
