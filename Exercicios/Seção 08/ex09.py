def calcular_volume_cilindro(altura, raio):
    """
    Função que recebe a altura e o raio de um cilindro circular e calcula o seu volume.
    """
    import math

    volume = math.pi * raio**2 * altura
    return volume


altura = float(input("Insira a altura do cilindro: "))
raio = float(input("Insira o raio do cilindro: "))
volume = calcular_volume_cilindro(altura, raio)
print(volume)
