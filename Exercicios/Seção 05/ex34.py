nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

if faltas > 20:
    if nota >= 9.0:
        conceito = "B"
    elif nota >= 7.5:
        conceito = "C"
    elif nota >= 5.0:
        conceito = "D"
    elif nota >= 4.0:
        conceito = "E"
    else:
        conceito = "E"
else:
    if nota >= 9.0:
        conceito = "A"
    elif nota >= 7.5:
        conceito = "B"
    elif nota >= 5.0:
        conceito = "C"
    elif nota >= 4.0:
        conceito = "D"
    else:
        conceito = "E"

print("O conceito do aluno é:", conceito)
