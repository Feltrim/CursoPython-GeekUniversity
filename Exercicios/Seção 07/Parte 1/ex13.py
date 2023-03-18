valores = []
for i in range(5):
    valor = float(input("Digite um valor: "))
    valores.append(valor)

maior_valor = max(valores)
indice_maior_valor = valores.index(maior_valor)

menor_valor = min(valores)
indice_menor_valor = valores.index(menor_valor)

print("Maior valor:", maior_valor, "na posição", indice_maior_valor)
print("Menor valor:", menor_valor, "na posição", indice_menor_valor)
