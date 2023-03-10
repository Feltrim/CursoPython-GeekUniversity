nota = 0
soma = 0
qtd_notas = 0

while True:
    nota = float(input("Digite uma nota (entre 10 e 20): "))
    if nota >= 10 and nota <= 20:
        soma += nota
        qtd_notas += 1
    else:
        break

if qtd_notas == 0:
    print("Nenhuma nota válida foi digitada.")
else:
    media = soma / qtd_notas
    print("Média: {:.2f}".format(media))
