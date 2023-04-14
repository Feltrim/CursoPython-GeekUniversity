def main():
    nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

    with open(nome_arquivo_entrada, 'r') as arquivo_entrada, open(nome_arquivo_saida, 'w') as arquivo_saida:
        linhas = arquivo_entrada.readlines()

        for linha in reversed(linhas):
            linha_inversa = linha[::-1]
            arquivo_saida.write(linha_inversa)

    print(
        f"Arquivo '{nome_arquivo_entrada}' invertido e salvo como '{nome_arquivo_saida}'.")


if __name__ == '__main__':
    main()
