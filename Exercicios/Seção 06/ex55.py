n = int(input("Digite um inteiro não negativo: "))
count = 0
soma = 0
num = 2

while count < n:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        soma += num
        count += 1
    num += 1

print("A soma dos", n, "primeiros números primos é:", soma)
