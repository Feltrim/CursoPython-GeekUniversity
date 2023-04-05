def concatena_n_caracteres(str1, str2, n):
    str1_len = len(str1)
    str2_len = len(str2)

    n = min(n, str2_len)

    for i in range(n):
        str1 += str2[i]

    str1 += '\0'

    return str1
