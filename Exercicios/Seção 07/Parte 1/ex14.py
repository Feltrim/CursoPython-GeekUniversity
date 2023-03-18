valores = []
for i in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

iguais = []
for i in range(len(valores)):
    for j in range(i+1, len(valores)):
        if valores[i] == valores[j] and valores[i] not in iguais:
            iguais.append(valores[i])

if len(iguais) == 0:
    print("Não existem valores iguais.")
else:
    print("Valores iguais: ", end="")
    for valor in iguais:
        print(valor, end=" ")
