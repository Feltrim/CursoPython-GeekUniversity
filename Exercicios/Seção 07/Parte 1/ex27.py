numeros = []
primos = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

for i in range(len(numeros)):
    primo = True
    for j in range(2, numeros[i]):
        if numeros[i] % j == 0:
            primo = False
            break
    if primo and numeros[i] > 1:
        primos.append(numeros[i])

if len(primos) == 0:
    print("Não há números primos no vetor.")
else:
    print("Números primos e suas posições no vetor:")
    for i in range(len(primos)):
        pos = numeros.index(primos[i])
        print(f"{primos[i]} na posição {pos}")
