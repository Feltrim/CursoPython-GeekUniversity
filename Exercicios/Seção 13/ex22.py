def ordenar_notas(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    notas = [(line[:40], int(line[40:43]), int(line[43:46]), int(line[46:]))
             for line in lines]

    notas.sort()

    with open(output_file, 'w') as f:
        for nome, nota1, nota2, nota3 in notas:
            f.write(f'{nome}{nota1:3}{nota2:3}{nota3:3}\n')
