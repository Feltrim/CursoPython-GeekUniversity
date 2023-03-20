vetor = []
i = 1

while len(vetor) < 100:
    if i % 7 != 0 and i % 10 != 7:
        vetor.append(i)
    i += 1

print(vetor)
