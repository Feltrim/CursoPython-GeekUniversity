codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

if codigo == 100:
    preco = 1.20
    lanche = "Cachorro quente"
elif codigo == 101:
    preco = 1.30
    lanche = "Bauru Simples"
elif codigo == 102:
    preco = 1.50
    lanche = "Bauru com Ovo"
elif codigo == 103:
    preco = 1.20
    lanche = "Hambúrguer"
elif codigo == 104:
    preco = 1.70
    lanche = "Cheeseburguer"
elif codigo == 105:
    preco = 2.20
    lanche = "Suco"
elif codigo == 106:
    preco = 1.00
    lanche = "Refrigerante"
else:
    print("Código inválido")
    exit()

total = quantidade * preco
print(f"O lanche {lanche} custa R${preco:.2f} cada unidade")
print(f"O total a ser pago é de R${total:.2f}")
