vetor = []
for i in range(15):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

i = 0
while i < len(vetor):
    if vetor[i] == 0:
        j = i
        while j < len(vetor)-1:
            vetor[j] = vetor[j+1]
            j += 1
        vetor[j] = 0
    else:
        i += 1

print("Vetor compactado:", vetor)
