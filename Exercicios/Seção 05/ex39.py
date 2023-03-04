salario = float(input("Digite o salário atual do funcionário: "))
tempo_servico = int(
    input("Digite o tempo de serviço do funcionário (em anos): "))

reajuste = 0
bonus = 0

if salario <= 500:
    reajuste = 0.25
    if tempo_servico < 1:
        bonus = 0
elif salario <= 1000:
    reajuste = 0.2
    if tempo_servico >= 1 and tempo_servico <= 3:
        bonus = 100
elif salario <= 1500:
    reajuste = 0.15
    if tempo_servico >= 4 and tempo_servico <= 6:
        bonus = 200
elif salario <= 2000:
    reajuste = 0.1
    if tempo_servico >= 7 and tempo_servico <= 10:
        bonus = 300
else:
    reajuste = 0
    if tempo_servico > 10:
        bonus = 500

if reajuste == 0 and bonus == 0:
    print("O funcionário não tem direito a nenhum aumento.")
else:
    aumento = salario * reajuste + bonus
    salario_reajustado = salario + aumento
    print(
        f"O salário reajustado do funcionário é R$ {salario_reajustado:.2f}.")
