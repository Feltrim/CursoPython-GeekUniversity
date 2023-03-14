while True:
    r1 = float(input("Digite o valor de R1 (0 para sair): "))
    if r1 == 0:
        break
    r2 = float(input("Digite o valor de R2: "))
    r = 1/(1/r1 + 1/r2)
    print("A resistência equivalente é:", r)
