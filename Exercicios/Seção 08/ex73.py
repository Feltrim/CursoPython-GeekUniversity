def ler_habitantes():
    habitantes = []
    for i in range(5):
        habitante = {}
        habitante['sexo'] = input(
            f'Digite o sexo do {i+1}º habitante (M/F): ').upper()
        habitante['olhos'] = input(
            f'Digite a cor dos olhos do {i+1}º habitante (A/C): ').upper()
        habitante['cabelos'] = input(
            f'Digite a cor dos cabelos do {i+1}º habitante (L/P/C): ').upper()
        habitante['idade'] = int(
            input(f'Digite a idade do {i+1}º habitante: '))
        habitantes.append(habitante)
    return habitantes


def media_idade_olhos_castanhos_cabelos_pretos(habitantes):
    soma_idades = 0
    n = 0
    for habitante in habitantes:
        if habitante['olhos'] == 'C' and habitante['cabelos'] == 'P':
            soma_idades += habitante['idade']
            n += 1
    if n > 0:
        media = soma_idades / n
        return media
    else:
        return None


def maior_idade(habitantes):
    maior = habitantes[0]['idade']
    for habitante in habitantes:
        if habitante['idade'] > maior:
            maior = habitante['idade']
    return maior


def contar_mulheres_olhos_azuis_cabelos_louros(habitantes):
    count = 0
    for habitante in habitantes:
        if habitante['sexo'] == 'F' and habitante['idade'] >= 18 and habitante['idade'] <= 35 and habitante['olhos'] == 'A' and habitante['cabelos'] == 'L':
            count += 1
    return count
