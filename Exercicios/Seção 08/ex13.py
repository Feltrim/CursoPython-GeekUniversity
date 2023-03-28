def calculadora(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Operação inválida'
    elif operador == '*':
        return num1 * num2
    else:
        return 'Operador inválido'


num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
operador = input("Insira o operador ( +   -   /   * )")
x = calculadora(2, 3, '+')
print(x)
