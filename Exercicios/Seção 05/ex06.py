numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(
        f"O primeiro número ({numero1}) é maior. A diferença entre eles é {diferenca}.")
elif numero2 > numero1:
    diferenca = numero2 - numero1
    print(
        f"O segundo número ({numero2}) é maior. A diferença entre eles é {diferenca}.")
else:
    print("Os números são iguais.")
