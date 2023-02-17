v = float(input("Qual o valor da hora trabalhada?\nR$"))
h = int(input(("Quantas horas foram trabalhadas?\nR:")))
s = h * v
print(f"Para {h} horas trabalhadas mensalmente o salário é de R${s}")
print(f"Com reajuste de 10% o salário passa a ser R${s + s * 10 / 100}")
