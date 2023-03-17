vetor = []
for i in range(10):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

print("O vetor é: ", vetor)

maior_elemento = vetor[0]
posicao_maior = 0
for i in range(1, len(vetor)):
    if vetor[i] > maior_elemento:
        maior_elemento = vetor[i]
        posicao_maior = i

print("O maior elemento é:", maior_elemento)
print("Ele está na posição:", posicao_maior)
