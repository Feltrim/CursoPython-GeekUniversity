numero = int(input("Digite um número inteiro: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e por 5 simultaneamente.")
elif numero % 3 == 0:
    print("O número é divisível por 3.")
elif numero % 5 == 0:
    print("O número é divisível por 5.")
else:
    print("O número não é divisível por 3 nem por 5.")
