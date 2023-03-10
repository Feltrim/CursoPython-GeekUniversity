n = 100
soma = 0
soma_quadrados = 0

for i in range(1, n+1):
    soma += i

for i in range(1, n+1):
    soma_quadrados += i*i

diferenca = soma*soma - soma_quadrados

print("A diferença entre a soma dos quadrados e o quadrado da soma dos",
      n, "primeiros números naturais é:", diferenca)
