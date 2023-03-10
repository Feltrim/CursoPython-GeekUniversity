base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

if base <= 0 or altura <= 0:
    print("As medidas fornecidas não são válidas. Tente novamente.")
else:
    area = (base * altura) / 2
    print(f"A área do triângulo é {area}.")
