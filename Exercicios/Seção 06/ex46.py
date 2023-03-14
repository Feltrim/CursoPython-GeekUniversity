import random

numero_gerado = random.randint(1, 1000)
tentativas = 0

print("Bem-vindo ao jogo de adivinhação! O número gerado está entre 1 e 1000.")

while True:
    chute = int(input("Tente adivinhar o número: "))
    tentativas += 1

    if chute == numero_gerado:
        print(
            f"Parabéns! Você acertou o número em {tentativas} tentativa(s)!")
        break
    elif chute < numero_gerado:
        print("O número gerado é maior que o seu chute. Tente novamente!")
    else:
        print("O número gerado é menor que o seu chute. Tente novamente!")
