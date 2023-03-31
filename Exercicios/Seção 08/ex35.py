def fatorial_quadruplo(n):
    fat = 1
    for i in range(4, n+1, 4):
        fat *= i
    return fat
