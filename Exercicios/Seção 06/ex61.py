maior_palindromo = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        produto = i * j
        if str(produto) == str(produto)[::-1]:
            if produto > maior_palindromo:
                maior_palindromo = produto

print("Maior palíndromo feito a partir do produto de dois números de 3 dígitos:", maior_palindromo)
