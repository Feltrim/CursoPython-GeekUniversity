idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    categoria = "Infantil A"
elif idade <= 10:
    categoria = "Infantil B"
elif idade <= 13:
    categoria = "Juvenil A"
elif idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior"

print(f"O nadador está na categoria {categoria}.")
