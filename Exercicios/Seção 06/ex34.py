n = 20

resultado = n

encontrado = False
while not encontrado:
    divisivel = True
    for i in range(1, n + 1):
        if resultado % i != 0:
            divisivel = False
            break
    if divisivel:
        encontrado = True
    else:
        resultado += n

print(resultado)
