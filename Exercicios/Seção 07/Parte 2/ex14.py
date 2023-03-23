import random

cartela = []

while len(cartela) < 25:
    num = random.randint(0, 99)
    if num not in cartela:
        cartela.append(num)

for i in range(5):
    print(cartela[i*5:(i+1)*5])
