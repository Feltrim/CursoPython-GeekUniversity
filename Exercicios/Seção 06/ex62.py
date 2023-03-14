numeros = {
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa',
    100: 'cem',
    200: 'duzentos',
    300: 'trezentos',
    400: 'quatrocentos',
    500: 'quinhentos',
    600: 'seiscentos',
    700: 'setecentos',
    800: 'oitocentos',
    900: 'novecentos',
    1000: 'mil'
}

letras = 0

for i in range(1, 1001):
    palavra = ''
    if i == 1000:
        palavra = numeros[i]
    elif i >= 100:
        centena = i // 100
        palavra += numeros[centena * 100]
        if i % 100 > 0:
            palavra += 'e'
            i = i % 100
    if i in numeros:
        palavra += numeros[i]
    else:
        dezena = i // 10 * 10
        palavra += numeros[dezena]
        if i % 10 > 0:
            palavra += numeros[i % 10]
    letras += len(palavra)

print(letras)
