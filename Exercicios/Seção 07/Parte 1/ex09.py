vetor = []
for i in range(6):
    while True:
        valor = int(input("Digite um valor inteiro par: "))
        if valor % 2 == 0:
            vetor.append(valor)
            break

print("Os valores na ordem inversa são: ")
for i in range(len(vetor) - 1, -1, -1):
    print(vetor[i])
