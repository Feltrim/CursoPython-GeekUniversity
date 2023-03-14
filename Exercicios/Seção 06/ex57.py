a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

cont_primos = 0

for num in range(a, b+1):
    if num > 1:
        eh_primo = True
        for i in range(2, num):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            cont_primos += 1

print(f"Existem {cont_primos} números primos entre {a} e {b}")
