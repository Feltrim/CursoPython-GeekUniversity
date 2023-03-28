def consumo_km_litro(distancia_km, litros_consumidos):
    consumo = distancia_km / litros_consumidos
    if consumo < 8:
        return 'Venda o carro!'
    elif consumo < 12:
        return 'Econômico!'
    else:
        return 'Super econômico!'


distancia = float(input("Insira a distância em Km percorrida: "))
consumido = float(
    input("Insira a quantidade em Litros de combustivel gasto: "))
relacao = consumo_km_litro(distancia, consumido)
print(relacao)
