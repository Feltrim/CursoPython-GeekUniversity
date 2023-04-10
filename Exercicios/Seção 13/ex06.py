def contar_letras_arquivo(nome_arquivo):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    contagem = {letra: 0 for letra in alfabeto}

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            for caractere in linha:
                if caractere.isalpha():
                    letra = caractere.lower()
                    if letra in alfabeto:
                        contagem[letra] += 1

    return contagem


nome_arquivo = input("Digite o nome do arquivo: ")
contagem_letras = contar_letras_arquivo(nome_arquivo)

for letra, contagem in contagem_letras.items():
    print(f"A letra '{letra}' aparece {contagem} vezes no arquivo.")
