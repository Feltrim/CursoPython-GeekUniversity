a = int(input("Digite um número positivo menor que 10000: "))
b = int(input("Digite outro número positivo menor que 10000: "))

vetor_a = []
vetor_b = []

while a > 0:
    resto = a % 10
    vetor_a.append(resto)
    a = a // 10

while b > 0:
    resto = b % 10
    vetor_b.append(resto)
    b = b // 10

tamanho = max(len(vetor_a), len(vetor_b))
vetor_soma = [0] * tamanho

carry = 0
for i in range(tamanho):
    soma = carry
    if i < len(vetor_a):
        soma += vetor_a[i]
    if i < len(vetor_b):
        soma += vetor_b[i]
    if soma >= 10:
        carry = 1
        soma -= 10
    else:
        carry = 0
    vetor_soma[i] = soma

if carry == 1:
    vetor_soma.append(carry)

print("Vetor soma: ", end="")
for i in range(len(vetor_soma)-1, -1, -1):
    print(vetor_soma[i], end="")
print()
