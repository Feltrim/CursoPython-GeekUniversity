import math

numero = float(input("Digite um número real: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}.")
else:
    numero_ao_quadrado = numero ** 2
    print(f"{numero} ao quadrado é {numero_ao_quadrado}.")
