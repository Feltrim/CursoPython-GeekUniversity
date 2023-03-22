x = []
y = []

for i in range(5):
    x.append(int(input(f"Digite o {i+1}º número do vetor x: ")))

for i in range(5):
    y.append(int(input(f"Digite o {i+1}º número do vetor y: ")))

soma = []
for i in range(5):
    soma.append(x[i] + y[i])
print(f"Soma entre x e y: {soma}")

produto = []
for i in range(5):
    produto.append(x[i] * y[i])
print(f"Produto entre x e y: {produto}")

diferenca = []
for i in x:
    if i not in y:
        diferenca.append(i)
print(f"Diferença entre x e y: {diferenca}")

interseccao = []
for i in x:
    if i in y:
        interseccao.append(i)
print(f"Intersecção entre x e y: {interseccao}")

uniao = x.copy()
for i in y:
    if i not in uniao:
        uniao.append(i)
print(f"União entre x e y: {uniao}")
