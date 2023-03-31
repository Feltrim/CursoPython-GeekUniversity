def neperiano(num_termos):
    e = 0
    fatorial = 1
    for i in range(num_termos):
        e += 1/fatorial
        fatorial *= (i+1)
    return e
