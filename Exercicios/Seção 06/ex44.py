num = int(input("Digite um número positivo: "))

if num <= 0:
    print("O número precisa ser positivo!")
else:
    fibonacci = [0, 1]

    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print("Sequência Fibonacci até o número", num, ":")
    for i in range(len(fibonacci)-1):
        print(fibonacci[i], end=", ")
    print(fibonacci[-1])
