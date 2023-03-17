numeros = []
for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

quadrados = []
for numero in numeros:
    quadrado = numero ** 2
    quadrados.append(quadrado)

print("Vetor original: ", numeros)
print("Vetor dos quadrados: ", quadrados)
