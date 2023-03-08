n = int(input("Digite um número inteiro positivo par: "))

for i in range(n, -1, -2):
    if i % 2 == 0:
        print(i)
