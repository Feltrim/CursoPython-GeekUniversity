a = []
b = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número do vetor A: "))
    a.append(num)
    num = int(input(f"Digite o {i+1}º número do vetor B: "))
    b.append(num)

c = []
for i in range(10):
    c.append(a[i])
    c.append(b[i])

print("Vetor C:", c)
