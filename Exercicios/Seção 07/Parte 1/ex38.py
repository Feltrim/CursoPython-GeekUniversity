vetor = []

for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    inserido = False
    
    for j in range(len(vetor)):
        if valor < vetor[j]:
            vetor.insert(j, valor)
            inserido = True
            break
    
    if not inserido:
        vetor.append(valor)

print("Valores em ordem crescente:")
print(vetor)
