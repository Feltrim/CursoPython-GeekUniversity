contador = 0
pares = 0
numero = int(input("Digite um número inteiro: "))
while numero != 1000:
    contador += 1
    if numero % 2 == 0:
        pares += 1
    numero = int(input("Digite um número inteiro: "))

print("Foram lidos", contador, "números e", pares, "deles eram pares.")
