def count_primes(n):
    """
    Função que conta a quantidade de números primos abaixo de N.
    """
    count = 0

    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return count


n = int(input("Insira o valor de N: "))
count = count_primes(n)
print(f"A quantidade de números primos abaixo de {n} é {count}.")
