salario_carlos = float(input("Digite o salário de Carlos: "))

salario_joao = salario_carlos / 3

taxa_poupanca = 0.02
taxa_renda_fixa = 0.05

meses = 0

while salario_joao <= salario_carlos:
    meses += 1
    salario_carlos *= 1 + taxa_poupanca
    salario_joao *= 1 + taxa_renda_fixa

print(f"Levará {meses} meses para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.")
