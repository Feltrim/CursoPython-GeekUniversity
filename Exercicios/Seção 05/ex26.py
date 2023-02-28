distancia_km = float(input("Digite a distância percorrida em km: "))
litros_gasolina = float(
    input("Digite a quantidade de litros de gasolina consumidos: "))

consumo_km_l = distancia_km / litros_gasolina

if consumo_km_l < 8:
    print("Consumo:", consumo_km_l, "Km/l. Venda o carro!")
elif consumo_km_l < 14:
    print("Consumo:", consumo_km_l, "Km/l. Econômico")
else:
    print("Consumo:", consumo_km_l, "Km/l. Super econômico!")
