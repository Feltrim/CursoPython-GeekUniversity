data = input("Digite uma data no formato DD/MM/AAAA: ")

dia, mes, ano = map(int, data.split('/'))

bissexto = False
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    bissexto = True

if mes < 1 or mes > 12:
    print("Data inválida")
else:
    if mes == 2:
        if bissexto:
            ultimo_dia = 29
        else:
            ultimo_dia = 28
    elif mes in [4, 6, 9, 11]:
        ultimo_dia = 30
    else:
        ultimo_dia = 31

    if dia < 1 or dia > ultimo_dia:
        print("Data inválida")
    else:
        print("Data válida")
