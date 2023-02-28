import random

acertos = 0

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    resp = int(input(f"Qual é a soma de {a} + {b}? "))
    if resp == a + b:
        print("Resposta correta!")
        acertos += 1
    else:
        print(f"Resposta incorreta. A resposta correta é {a + b}.")

print(f"Você acertou {acertos} de 5 perguntas.")
