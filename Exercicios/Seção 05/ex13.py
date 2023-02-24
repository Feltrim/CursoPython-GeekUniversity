nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + 2*nota3)/4

print("A média do aluno é:", media)

if media >= 60:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
