n = int(input("Digite um valor inteiro e positivo para n: "))
h = 0

for i in range(1, n+1):
    h += 1/i

print("O valor de H(n) é:", h)
