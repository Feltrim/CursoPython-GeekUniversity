def verifica_quadrado_perfeito(numero):
    """
    Função que verifica se um número é um quadrado perfeito.
    Retorna True se o número é um quadrado perfeito e False caso contrário.
    """
    if numero < 0:
        return False
    elif numero == 0:
        return True
    else:
        raiz = int(numero ** 0.5)
        return raiz ** 2 == numero


x = verifica_quadrado_perfeito(int(input("Insira um número inteiro: ")))
print(x)
