def encontrar_maior(numero1, numero2):
    """
    Função que recebe dois números fornecidos pelo usuário e retorna o maior.
    """
    if numero1 > numero2:
        return numero1
    else:
        return numero2


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
maior = encontrar_maior(numero1, numero2)
print(f"O maior número é: {maior}")
