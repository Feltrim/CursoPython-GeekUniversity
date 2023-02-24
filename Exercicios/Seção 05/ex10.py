altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M/F): ")

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é:", peso_ideal, "kg")
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é:", peso_ideal, "kg")
else:
    print("Sexo inválido.")
