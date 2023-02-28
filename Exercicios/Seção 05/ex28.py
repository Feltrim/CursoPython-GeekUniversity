import math

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

tipo_media = input(
    """Digite a letra correspondente ao tipo de média desejada:\n
    a) Geométrica
    b) Ponderada
    c) Harmônica
    d) Aritmética\n
Sua escolha: """)

if tipo_media == 'a':
    media = math.pow(a*b*c, 1/3)
elif tipo_media == 'b':
    media = (a*5 + b*3 + c*2) / (5+3+2)
elif tipo_media == 'c':
    media = 3 / (1/a + 1/b + 1/c)
elif tipo_media == 'd':
    media = (a + b + c) / 3
else:
    print("Tipo de média inválido.")
    media = None
if media is not None:
    print(f"A média {tipo_media} dos números {a}, {b} e {c} é {media}.")
