def dec2bin(num):
    return bin(num)[2:]


numeros = [23, 45, 67, 89, 123, 456, 789, 1011, 1213, 1415]

arquivo = open("numeros_bin.txt", "w")

for num in numeros:
    binario = dec2bin(num)
    arquivo.write(binario + "\n")

arquivo.close()
