base_maior = float(input("Digite a medida da base maior do trapézio: "))
base_menor = float(input("Digite a medida da base menor do trapézio: "))
altura = float(input("Digite a medida da altura do trapézio: "))

if base_maior <= 0 or base_menor <= 0:
    print("As bases do trapézio devem ser maiores que zero.")
else:
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area:.2f}")
