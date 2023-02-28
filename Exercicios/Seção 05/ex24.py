valor = float(input("Digite o valor do produto: R$"))
estado = input("Digite o estado destino do produto (MG, SP, RJ ou MS): ")

if estado == "MG":
    imposto = 0.07
elif estado == "SP":
    imposto = 0.12
elif estado == "RJ":
    imposto = 0.15
elif estado == "MS":
    imposto = 0.08
else:
    print("Erro: estado inválido")
    imposto = 0

preco_final = valor * (1 + imposto)
print("O preço final do produto é R${:.2f}".format(preco_final))
