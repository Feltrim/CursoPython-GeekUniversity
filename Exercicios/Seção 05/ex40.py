custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

if custo_fabrica <= 12000:
    comissao = 0.05 * custo_fabrica
    impostos = 0
elif custo_fabrica <= 25000:
    comissao = 0.1 * custo_fabrica
    impostos = 0.15 * custo_fabrica
else:
    comissao = 0.15 * custo_fabrica
    impostos = 0.2 * custo_fabrica

custo_consumidor = custo_fabrica + comissao + impostos

print("O custo ao consumidor é de R$", custo_consumidor)
