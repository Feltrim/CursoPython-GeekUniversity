s = 0

for n in range(5):
    fatorial = 1
    for i in range(2*n, 1, -1):
        fatorial *= i

    termo = n / fatorial

    s += termo

print(f"S = {s:.4f}")
