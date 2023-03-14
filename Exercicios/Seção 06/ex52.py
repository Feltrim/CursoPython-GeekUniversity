valor = int(input('Informe o valor do saque: R$ '))

notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []

for nota in notas:
    qtd = valor // nota
    valor = valor % nota
    quantidades.append(qtd)

print('Quantidade de notas necessárias:')
for i in range(len(notas)):
    print('{} nota(s) de R$ {}: {:.0f}'.format(
        quantidades[i], notas[i], quantidades[i]*notas[i]))
