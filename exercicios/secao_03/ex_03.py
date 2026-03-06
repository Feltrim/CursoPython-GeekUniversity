"""
Feito por: Vitor Feltrim

Curso Python - Geek University
Seção 03 - Exercício 03

Faça um programa que recebe três valores e apresente
a soma dos quadrados dos valores lidos.
"""


ler_primeiro_numero = int(input("Insira o primeiro número inteiro: "))
ler_segundo_numero = int(input("Insira o segundo número inteiro: "))
ler_terceiro_numero = int(input("Insira o terceiro número inteiro: "))

quadrado_primeiro_numero = ler_primeiro_numero
quadrado_segundo_numero = ler_segundo_numero
quadrado_terceiro_numero = ler_terceiro_numero

quadrado_primeiro_numero *= quadrado_primeiro_numero
quadrado_segundo_numero *= quadrado_segundo_numero
quadrado_terceiro_numero *= quadrado_terceiro_numero

print(f"A soma dos quadrados dos números é: {quadrado_primeiro_numero + quadrado_segundo_numero + quadrado_terceiro_numero}")
