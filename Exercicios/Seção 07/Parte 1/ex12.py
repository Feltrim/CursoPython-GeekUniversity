valores = []
for i in range(5):
    valor = float(input("Digite um valor: "))
    valores.append(valor)

print("Valores lidos:", valores)

maior_valor = max(valores)

menor_valor = min(valores)

media_valores = sum(valores) / len(valores)

print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)
print("Média dos valores:", media_valores)
