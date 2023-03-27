import math


def calcula_volume_esfera(raio):
    """
    Função que calcula o volume de uma esfera de raio R.
    """
    volume = (4/3) * math.pi * raio ** 3
    return volume


def test_calcula_volume_esfera():
    assert calcula_volume_esfera(0) == 0
    assert calcula_volume_esfera(1) == 4.1887902047863905
    assert calcula_volume_esfera(2) == 33.510321638291124
    assert calcula_volume_esfera(5) == 523.5987755982989
    print("Todos os testes passaram.")


test_calcula_volume_esfera()
