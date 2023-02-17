segundos = int(input("Digite um valor em segundos: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60
print(f"{horas} horas, {minutos} minutos e {segundos_finais} segundos.")
