import math

n = int(input("Digite um número inteiro e positivo: "))
e = 1

for i in range(1, n+1):
    fatorial = math.factorial(i)
    e += 1/fatorial

print("O valor de E é:", e)
