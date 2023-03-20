import math

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

media = sum(vetor) / len(vetor)

soma_quadrados = sum([(x - media) ** 2 for x in vetor])

desvio_padrao = math.sqrt(soma_quadrados / (len(vetor) - 1))

print(f"O desvio padrão do vetor é {desvio_padrao:.2f}")
