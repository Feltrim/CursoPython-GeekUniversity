def celsius_para_fahrenheit(celsius):
    """
    Função que recebe uma temperatura em graus Celsius como parâmetro e a converte em graus Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = float(input("Insira uma temperatura em Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print(fahrenheit)
