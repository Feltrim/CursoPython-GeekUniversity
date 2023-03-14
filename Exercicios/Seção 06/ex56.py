soma = 0

for num in range(2, 2000000):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        soma += num

print(soma)
