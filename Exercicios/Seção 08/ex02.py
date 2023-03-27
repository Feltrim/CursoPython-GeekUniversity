def data_por_extenso(dia, mes, ano):
    """
    Função que recebe a data atual (dia, mês e ano em inteiro) e exibe-a na tela no formato textual por extenso.
    """
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    print(f"{dia} de {meses[mes - 1]} de {ano}")


dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
data_por_extenso(dia, mes, ano)
