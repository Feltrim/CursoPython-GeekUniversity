altura = float(input("Digite a altura da pessoa: "))
peso = float(input("Digite o peso da pessoa: "))

if altura < 1.2:
    if peso <= 60:
        print("Classificação: A")
    elif peso <= 90:
        print("Classificação: D")
    else:
        print("Classificação: G")
elif altura <= 1.7:
    if peso <= 60:
        print("Classificação: B")
    elif peso <= 90:
        print("Classificação: E")
    else:
        print("Classificação: H")
else:
    if peso <= 60:
        print("Classificação: C")
    elif peso <= 90:
        print("Classificação: F")
    else:
        print("Classificação: I")
