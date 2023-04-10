arq = open('arq.txt', 'w')

while True:
    caractere = input(
        "Digite um caractere para gravar no arquivo ou '0' para sair: ")
    if caractere == '0':
        break
    arq.write(caractere)

arq.close()

arq = open('arq.txt', 'r')

for caractere in arq.read():
    print(caractere)

arq.close()
