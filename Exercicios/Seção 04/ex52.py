apostador1 = float(input("Digite o valor que o apostador 1 investiu: "))
apostador2 = float(input("Digite o valor que o apostador 2 investiu: "))
apostador3 = float(input("Digite o valor que o apostador 3 investiu: "))
premio = float(input("Digite o valor do prêmio: "))

total_aposta = apostador1 + apostador2 + apostador3

pct_apostador1 = apostador1 / total_aposta
pct_apostador2 = apostador2 / total_aposta
pct_apostador3 = apostador3 / total_aposta

valor_apostador1 = pct_apostador1 * premio
valor_apostador2 = pct_apostador2 * premio
valor_apostador3 = pct_apostador3 * premio

print(f"O apostador 1 ganhou R${valor_apostador1:.2f}")
print(f"O apostador 2 ganhou R${valor_apostador2:.2f}")
print(f"O apostador 3 ganhou R${valor_apostador3:.2f}")
