def triangulo_lateral(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('*', end='')
        print()
    for i in range(n-1, 0, -1):
        for j in range(1, i+1):
            print('*', end='')
        print()


n = int(input("Digite um valor para n: "))
triangulo_lateral(n)
