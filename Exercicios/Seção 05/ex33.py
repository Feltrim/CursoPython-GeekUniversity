preco_antigo = float(input("Digite o preço antigo: "))

if preco_antigo <= 50:
    percentual_aumento = 0.05
elif preco_antigo <= 100:
    percentual_aumento = 0.1
else:
    percentual_aumento = 0.15

preco_novo = preco_antigo * (1 + percentual_aumento)

if preco_novo <= 80:
    mensagem = "Barato"
elif preco_novo <= 120:
    mensagem = "Normal"
elif preco_novo <= 200:
    mensagem = "Caro"
else:
    mensagem = "Muito caro"

print("O preço antigo era R$ {:.2f}".format(preco_antigo))
print("O preço novo é R$ {:.2f}".format(preco_novo))
print("Mensagem: {}".format(mensagem))
