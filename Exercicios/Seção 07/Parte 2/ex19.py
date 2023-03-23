matriz = [[0]*4 for i in range(5)]
maior_nota = 0
pos_maior_nota = 0
soma_notas = 0

for i in range(5):
    print(f"Informe as informações do {i+1}º aluno:")
    for j in range(3):
        if j == 0:
            matriz[i][j] = int(input("Número de matrícula: "))
        elif j == 1:
            matriz[i][j] = int(input("Média das provas: "))
        else:
            matriz[i][j] = int(input("Média dos trabalhos: "))

for i in range(5):
    nota_final = matriz[i][1] + matriz[i][2]
    matriz[i][3] = nota_final
    soma_notas += nota_final
    if nota_final > maior_nota:
        maior_nota = nota_final
        pos_maior_nota = i

print(
    f"A matrícula do aluno com a maior nota final é: {matriz[pos_maior_nota][0]}")

media_notas = soma_notas / 5
print(f"A média aritmética das notas finais é: {media_notas:.2f}")
