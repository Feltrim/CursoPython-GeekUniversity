vetor = []
for i in range(6):
    valor = int(input("Digite um valor inteiro: "))
    vetor.append(valor)

print("Os valores na ordem inversa são: ")
for i in range(len(vetor) - 1, -1, -1):
    print(vetor[i])
