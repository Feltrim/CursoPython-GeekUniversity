inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))
soma = 0

if inicio > fim:
    print("Intervalo de valores inválido")
else:
    for i in range(inicio, fim+1):
        if i % 2 == 1:
            soma += i

    print(f"A soma dos números ímpares no intervalo [{inicio}, {fim}] é: {soma}")
