def maior_fator_primo(num):
    """
    Retorna o maior fator primo de um número fornecido pelo usuário.
    """
    def eh_primo(num):
        """
        Verifica se um número é primo.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(num, 1, -1):
        if num % i == 0 and eh_primo(i):
            return i
    return None


num = int(input("Digite um número: "))
maior_fator = maior_fator_primo(num)
if maior_fator is None:
    print("O número {} não possui fatores primos.".format(num))
else:
    print("O maior fator primo de {} é {}.".format(num, maior_fator))
