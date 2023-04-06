def reduz(a, b):
    if b == 0:
        raise ValueError("Denominador não pode ser zero!")
    mdc = abs(a)
    n = abs(b)
    while n != 0:
        r = mdc % n
        mdc = n
        n = r
    return (a // mdc, b // mdc)


def neg(x):
    return (-x[0], x[1])


def soma(x, y):
    a = x[0] * y[1] + y[0] * x[1]
    b = x[1] * y[1]
    return reduz(a, b)


def mult(x, y):
    a = x[0] * y[0]
    b = x[1] * y[1]
    return reduz(a, b)


def div(x, y):
    if y[0] == 0:
        raise ValueError("Divisão por zero!")
    a = x[0] * y[1]
    b = x[1] * y[0]
    return reduz(a, b)
