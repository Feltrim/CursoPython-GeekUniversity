habitantes = int(input("Informe o número de habitantes: "))
valor_kwh = float(input("Informe o valor do kwh: "))

maior_consumo = menor_consumo = soma_consumo = 0

total_residencial = total_comercial = total_industrial = 0

for i in range(1, habitantes + 1):
    consumo = float(input(f"Informe o consumo do habitante {i}: "))
    codigo = int(input(
        f"Informe o código do consumidor do habitante {i} (1-Residencial, 2-Comercial, 3-Industrial): "))

    if i == 1:
        maior_consumo = menor_consumo = consumo
    else:
        if consumo > maior_consumo:
            maior_consumo = consumo
        if consumo < menor_consumo:
            menor_consumo = consumo

    soma_consumo += consumo

    if codigo == 1:
        total_residencial += consumo
    elif codigo == 2:
        total_comercial += consumo
    elif codigo == 3:
        total_industrial += consumo

media_consumo = soma_consumo / habitantes

print(f"Maior consumo: {maior_consumo}")
print(f"Menor consumo: {menor_consumo}")
print(f"Média do consumo dos habitantes: {media_consumo}")
print(f"Total de consumo residencial: {total_residencial}")
print(f"Total de consumo comercial: {total_comercial}")
print(f"Total de consumo industrial: {total_industrial}")
