numeros = []
i = 0

while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero not in numeros:
        numeros.append(numero)
        i += 1
    else:
        print("Número repetido. Digite outro número.")

print("Números digitados: ", numeros)
