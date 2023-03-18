
vetor = []
for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

r = int(input("Digite o número r: "))

x = int(input("Digite o número x: "))

quantidade_multiplos = 0
for numero in vetor:
    if numero % x == 0:
        quantidade_multiplos += 1

if quantidade_multiplos > 0:
    print(f"Existem {quantidade_multiplos} múltiplos de {x} no vetor:")
    for numero in vetor:
        if numero % x == 0:
            print(numero)
else:
    print(f"Não existem múltiplos de {x} no vetor.")
