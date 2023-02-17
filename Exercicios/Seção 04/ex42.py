s = float(input("Qual o salário-base do funcionário?\nR$"))
i = s * 7 / 100
g = s + s * 5 / 100
print(
    f"O salário descontando os impostos e somando a gratificação é de R${g - i}")
