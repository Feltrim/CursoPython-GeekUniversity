def potencia(x, z):
    resultado = 1
    for i in range(z):
        resultado *= x
    return resultado

x = int(input("Digite o valor de X: "))
z = int(input("Digite o valor de Z: "))

print("Resultado:", potencia(x, z))
