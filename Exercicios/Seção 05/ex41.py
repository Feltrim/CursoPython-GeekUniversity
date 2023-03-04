peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Seu IMC é {:.2f} e você está abaixo do peso.".format(imc))
elif imc < 25:
    print("Seu IMC é {:.2f} e você está com peso normal.".format(imc))
elif imc < 30:
    print("Seu IMC é {:.2f} e você está com sobrepeso.".format(imc))
elif imc < 35:
    print("Seu IMC é {:.2f} e você está com obesidade grau 1.".format(imc))
elif imc < 40:
    print("Seu IMC é {:.2f} e você está com obesidade grau 2.".format(imc))
else:
    print("Seu IMC é {:.2f} e você está com obesidade grau 3.".format(imc))
