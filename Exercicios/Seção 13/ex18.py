nome_arquivo = input("Digite o nome do arquivo: ")

total = 0.0

with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        dados = linha.split()
        preco = float(dados[1])
        total += preco

print(f"O total da compra é: R${total:.2f}")
