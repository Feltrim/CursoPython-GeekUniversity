def verificar_positivo_negativo(numero):
    """
    Função que recebe um número e retorna 1 se for positivo, -1 se for negativo e 0 se for igual a 0.
    """
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0


x = verificar_positivo_negativo(int(input("Digite um número inteiro: ")))
print(x)
