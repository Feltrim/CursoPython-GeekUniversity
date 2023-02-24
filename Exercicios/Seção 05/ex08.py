nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 < 0 or nota1 > 10:
    print("Nota 1 inválida! Deve ser um valor entre 0.0 e 10.0")
    exit()

if nota2 < 0 or nota2 > 10:
    print("Nota 2 inválida! Deve ser um valor entre 0.0 e 10.0")
    exit()

media = (nota1 + nota2) / 2

print("A média das notas é:", media)
