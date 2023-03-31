def simplifica(numerador, denominador):
    def mdc(a, b):
        if b == 0:
            return a
        return mdc(b, a % b)

    divisor = mdc(numerador, denominador)
    return numerador // divisor, denominador // divisor
