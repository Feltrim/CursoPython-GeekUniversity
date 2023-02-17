num = int(input("Digite um número inteiro de três dígitos: "))
centenas = num // 100
dezenas = (num // 10) % 10
unidades = num % 10
invertido = unidades * 100 + dezenas * 10 + centenas
print(f"O número invertido é {invertido}.")
