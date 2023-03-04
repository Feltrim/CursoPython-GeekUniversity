from datetime import datetime

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

if ano > datetime.now().year:
    print("Data inválida: ano inválido.")
elif ano == datetime.now().year and mes > datetime.now().month:
    print("Data inválida: mês inválido para o ano atual.")
elif ano == datetime.now().year and mes == datetime.now().month and dia > datetime.now().day:
    print("Data inválida: dia inválido para o mês e ano atual.")
else:
    if mes < 1 or mes > 12:
        print("Data inválida: mês inválido.")
    else:
        if mes in [4, 6, 9, 11] and (dia < 1 or dia > 30):
            print("Data inválida: dia inválido para o mês.")
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                if dia < 1 or dia > 29:
                    print("Data inválida: dia inválido para o mês.")
            else:
                if dia < 1 or dia > 28:
                    print("Data inválida: dia inválido para o mês.")
        elif dia < 1 or dia > 31:
            print("Data inválida: dia inválido para o mês.")
        else:
            print("Data válida.")
