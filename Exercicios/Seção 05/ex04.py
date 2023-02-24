numero = float(input("Digite um número: "))

if numero > 0:
    quadrado = numero ** 2
    raiz_quadrada = numero ** 0.5
    print(f"O número ao quadrado é {quadrado:.2f}.")
    print(f"A raiz quadrada do número é {raiz_quadrada:.2f}.")
else:
    print("O número digitado não é positivo.")
