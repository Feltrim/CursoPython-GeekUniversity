idades = []
idade = int(input("Digite a idade: "))

while idade != 0:
    idades.append(idade)
    idade = int(input("Digite a idade: "))

if len(idades) > 0:
    media = sum(idades) / len(idades)
    print("A média das idades é:", media)
else:
    print("Não foi informada nenhuma idade.")
