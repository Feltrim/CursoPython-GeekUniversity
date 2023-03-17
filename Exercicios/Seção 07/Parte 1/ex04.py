vetor = []
for i in range(8):
    valor = float(input("Digite um valor para a posição {}: ".format(i)))
    vetor.append(valor)

x = int(input("Digite o valor de X (entre 0 e 7): "))
y = int(input("Digite o valor de Y (entre 0 e 7): "))

soma = vetor[x] + vetor[y]

print("A soma dos valores nas posições {} e {} do vetor é: {}".format(x, y, soma))
