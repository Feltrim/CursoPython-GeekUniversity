import random

n = int(input("Digite o número de vezes que deseja simular o lançamento dos dados: "))

for i in range(n):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    if d1 > d2:
        print(f"({d1}, {d2}) >")
    elif d1 < d2:
        print(f"({d1}, {d2}) <")
    else:
        print(f"({d1}, {d2}) =")
