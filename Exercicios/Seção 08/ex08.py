def calcular_hipotenusa(a, b):
    """
    Função que recebe os valores dos catetos a e b de um triângulo retângulo e calcula o valor da hipotenusa.
    """
    hipotenusa = ((a ** 2) + (b ** 2)) ** 0.5
    return hipotenusa


a = float(input("Insira o valor do cateto a: "))
b = float(input("Insira o valor do cateto b: "))
hipotenusa = calcular_hipotenusa(a, b)
print(hipotenusa)
