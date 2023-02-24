import math

num = int(input("Digite um número inteiro: "))

if num < 0:
    print("Número inválido")
else:
    log_num = math.log10(num)
    print(f"O logaritmo de {num} é {log_num:.2f}")
