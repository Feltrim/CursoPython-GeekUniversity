a, b = 1, 2
soma_par = 2

while b <= 4000000:
    a, b = b, a + b

    if b % 2 == 0:
        soma_par += b

print("A soma dos termos de valor par da sequência de Fibonacci até 4 milhões é:", soma_par)
