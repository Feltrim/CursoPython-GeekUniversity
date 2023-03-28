def calcular_media(nota1, nota2, nota3, letra):
    """
    Função que recebe três notas de um aluno e uma letra indicando o tipo de média a ser calculada.
    A letra 'A' indica média aritmética e 'P' indica média ponderada com pesos 5, 3 e 2.
    """
    if letra == 'A':
        media = (nota1 + nota2 + nota3) / 3
    elif letra == 'P':
        media = (nota1*5 + nota2*3 + nota3*2) / 10
    else:
        print("Letra inválida. Digite 'A' ou 'P'.")
        return None

    return media


nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
letra = input(
    "Insira 'A' para Média Aritmética e 'P' para Média Ponderada: ")
media = calcular_media(nota1, nota2, nota3, letra)
print(f"A média do aluno é: {media}")
