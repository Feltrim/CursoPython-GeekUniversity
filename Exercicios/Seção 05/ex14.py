nota_lab = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
nota_sem = float(input("Digite a nota da avaliação semestral (0 a 10): "))
nota_final = float(input("Digite a nota do exame final (0 a 10): "))

media = (nota_lab * 2 + nota_sem * 3 + nota_final * 5) / 10

if media < 3:
    print("Aluno reprovado.")
elif media < 5:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")
