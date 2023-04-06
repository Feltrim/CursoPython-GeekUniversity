def mdc(a, b):
    """
    Função que calcula o máximo divisor comum entre dois números usando o algoritmo de Euclides
    """
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def simplificar_fracao(p, q):
    """
    Função que simplifica uma fração p/q
    """
    divisor = mdc(p, q)
    p = p // divisor
    q = q // divisor
    return p, q


def somar_fracoes(p1, q1, p2, q2):
    """
    Função que soma duas frações p1/q1 e p2/q2
    """
    denominador_comum = q1 * q2
    numerador1 = p1 * q2
    numerador2 = p2 * q1
    numerador_soma = numerador1 + numerador2
    return simplificar_fracao(numerador_soma, denominador_comum)


def subtrair_fracoes(p1, q1, p2, q2):
    """
    Função que subtrai duas frações p1/q1 e p2/q2
    """
    denominador_comum = q1 * q2
    numerador1 = p1 * q2
    numerador2 = p2 * q1
    numerador_diferenca = numerador1 - numerador2
    return simplificar_fracao(numerador_diferenca, denominador_comum)


def multiplicar_fracoes(p1, q1, p2, q2):
    """
    Função que multiplica duas frações p1/q1 e p2/q2
    """
    numerador_produto = p1 * p2
    denominador_produto = q1 * q2
    return simplificar_fracao(numerador_produto, denominador_produto)


def dividir_fracoes(p1, q1, p2, q2):
    """
    Função que divide duas frações p1/q1 por p2/q2
    """
    numerador_divisao = p1 * q2
    denominador_divisao = q1 * p2
    return simplificar_fracao(numerador_divisao, denominador_divisao)


p1 = int(input("Digite o numerador da primeira fração: "))
q1 = int(input("Digite o denominador da primeira fração: "))
p2 = int(input("Digite o numerador da segunda fração: "))
q2 = int(input("Digite o denominador da segunda fração: "))

p1, q1 = simplificar_fracao(p1, q1)
p2, q2 = simplificar_fracao(p2, q2)

soma = somar_fracoes(p1, q1, p2, q2)
diferenca = subtrair_fracoes(p1, q1, p2, q2)
produto = multiplicar_fracoes(p1, q1, p2, q2)
divisao = dividir_fracoes(p1, q1, p2, q2)

print("Soma: {}/{}".format(soma[0], soma[1]))
print("Subtração: {}/{}".format(diferenca[0], diferenca[1]))
print("Produto: {}/{}".format(produto[1], produto[2]))
print("Quociente: {}/{}".format(divisao[1], divisao[2]))
