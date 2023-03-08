numero = int(input("Digite um número entre 100 e 999: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

print(f"Centenas: {centenas}")
print(f"Dezenas: {dezenas}")
print(f"Unidades: {unidades}")
