A = []
for i in range(11):
    num = float(input(f"Digite o {i+1}º número: "))
    A.append(num)

for i in range(5):
    for j in range(i+1, 6):
        if A[i] > A[j]:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

for i in range(6, 11):
    for j in range(i+1, 11):
        if A[i] < A[j]:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

print("Vetor ordenado:")
for num in A:
    print(num, end=" ")
