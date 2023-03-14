altura_chico = 1.50
altura_ze = 1.10
anos = 0

while altura_ze <= altura_chico:
    altura_chico += 0.02
    altura_ze += 0.03
    anos += 1

print(f"Serão necessários {anos} anos para que Zé seja maior que Chico.")
