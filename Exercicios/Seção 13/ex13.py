arquivo = open('cadastro.txt', 'w')

while True:
    nome = input('Digite o nome: ')
    if nome == '0':
        break
    telefone = input('Digite o telefone: ')
    if telefone == '0':
        break
    arquivo.write(nome + ' ' + telefone + '\n')

arquivo.close()
