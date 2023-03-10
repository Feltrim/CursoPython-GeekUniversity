n = int(input("Digite um número: "))

i = n + 1
while True:
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        print("O primeiro múltiplo de 11, 13 ou 17 após", n, "é", i)
        break
    i += 1
