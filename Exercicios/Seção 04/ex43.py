vp = float(input("Insira o valor do produto\nR$"))
vd = vp - vp * 10 / 100
vpar = vp / 3
print(
    f"Com um desconto de 10% comprado à vista o produto passa a custar R${vd}")
print(f"O valor da parcela em 3x sem juros é de R${vpar}")
print(f"A comissão do vendedor na compra à vista será de R${vd * 5 / 100}")
print(
    f"A comissão do vendedor na compra parcelada será de R${vpar * 5 / 100}")
