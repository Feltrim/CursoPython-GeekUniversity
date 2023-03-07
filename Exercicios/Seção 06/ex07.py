soma = 0
count = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    if num > 0:
        soma += num
        count += 1

if count == 0:
    print("Não foram digitados números positivos.")
else:
    media = soma / count
    print(f"A média dos {count} números positivos é {media:.2f}.")
