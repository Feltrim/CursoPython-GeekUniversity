n = int(input("Digite um número inteiro N: "))
count = 0
for i in range(1, 2*n, 2):
    print(i, end=" ")
    count += 1
    if count == n:
        break
