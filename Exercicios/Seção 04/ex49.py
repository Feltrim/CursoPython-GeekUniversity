hora_inicio = int(input("Digite a hora de início da experiência (0 a 23): "))
minuto_inicio = int(
    input("Digite o minuto de início da experiência (0 a 59): "))
segundo_inicio = int(
    input("Digite o segundo de início da experiência (0 a 59): "))
duracao_segundos = int(
    input("Digite a duração da experiência em segundos: "))
segundos_totais = hora_inicio * 3600 + minuto_inicio * \
    60 + segundo_inicio + duracao_segundos
hora_fim = segundos_totais // 3600 % 24
minuto_fim = segundos_totais // 60 % 60
segundo_fim = segundos_totais % 60
print(
    f"O término da experiência será às {hora_fim:02d}:{minuto_fim:02d}:{segundo_fim:02d}")
