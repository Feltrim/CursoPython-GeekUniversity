maior = menor = 0
while True:
    num = int(input("Digite um número inteiro (negativo para sair): "))
    if num < 0:
        break
    if num == 0:
        print("Zero não é um número válido.")
        continue
    if num > maior or maior == 0:
        maior = num
    if num < menor or menor == 0:
        menor = num

print("Maior número digitado:", maior)
print("Menor número digitado:", menor)
