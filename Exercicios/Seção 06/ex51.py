ano_atual = 2023
salario_atual = 2000
aumento_percentual = 0.015

for ano in range(1996, ano_atual):
    aumento_percentual *= 2
    aumento = salario_atual * aumento_percentual
    salario_atual += aumento

print(f"Salário atual do funcionário em {ano_atual}: R${salario_atual:.2f}")
