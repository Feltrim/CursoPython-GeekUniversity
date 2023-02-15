from math import sqrt

c1 = int(input("Insira a medida do primeiro cateto"))
c2 = int(input("Insira a medida do segundo cateto"))
print(f"A hipotenusa desse triângulo mede {sqrt((c1 * c1) + (c2 * c2))}")
