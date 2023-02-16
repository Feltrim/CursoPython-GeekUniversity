d = int(input("O encanador trabalhou por quantos dias?\nR: "))
s = d * 30
print(f"O encanador receberá R${s} por {d} dias trabalhados")
print(
    f"Descontando do Imposto de Renda, o encanador receberá R${(s - s * 8 / 100) }")
