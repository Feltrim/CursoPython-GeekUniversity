for num in range(1000, 10000):
    alta_ordem = num // 100
    baixa_ordem = num % 100
    if (alta_ordem + baixa_ordem) ** 2 == num:
        print(num)
