vetor = [0] * 5

for i in range(5):
    vetor[i] = float(input(f"Digite o {i+1}º valor: "))

while True:
    codigo = int(input("\nDigite o código: "))

    if codigo == 0:
        print("\nPrograma finalizado.")
        break
    elif codigo == 1:
        print("\nVetor na ordem direta: ", vetor)
    elif codigo == 2:
        print("\nVetor na ordem inversa: ", vetor[::-1])
    else:
        print("\nCódigo inválido.")
