num = int(input("Digite um número inteiro: "))

if num <= 1:
    print("Número inválido.")
else:
    for i in range(2, num//2 + 1):
        if num % i == 0:
            print(num, "não é primo.")
            break
    else:
        print(num, "é primo.")
