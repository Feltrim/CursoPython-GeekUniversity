def converte_para_segundos(horas, minutos, segundos):
    """
    Função que recebe horas, minutos e segundos como parâmetros e os converte em segundos.
    """
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos


horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total_segundos = converte_para_segundos(horas, minutos, segundos)
print(total_segundos)
