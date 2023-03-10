n = int(input("Digite o valor de n: "))
i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

multiplos = []
k = 0

while len(multiplos) < n:
    if k % i == 0 or k % j == 0:
        multiplos.append(k)
    k += 1

print(multiplos)
