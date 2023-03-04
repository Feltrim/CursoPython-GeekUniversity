chegada_hora, chegada_minuto = map(int, input(
    'Digite a hora e minuto de chegada: ').split())
partida_hora, partida_minuto = map(int, input(
    'Digite a hora e minuto de partida: ').split())

chegada = chegada_hora * 60 + chegada_minuto
partida = partida_hora * 60 + partida_minuto

permanencia = partida - chegada
if permanencia < 0:
    permanencia += 24 * 60

horas = (permanencia + 59) // 60

if horas <= 2:
    valor = horas * 1
elif horas <= 4:
    valor = 2 * 1 + (horas - 2) * 1.4
else:
    valor = 2 * 1 + 2 * 1.4 + (horas - 4) * 2

print('O valor a ser pago é R$ {:.2f}'.format(valor))
