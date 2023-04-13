import pickle

estoque = {}


def entrada_produto(codigo, descricao, quantidade):
    if codigo in estoque:
        estoque[codigo]['quantidade'] += quantidade
    else:
        estoque[codigo] = {'descricao': descricao, 'quantidade': quantidade}


def retirada_produto(codigo, quantidade):
    if codigo in estoque:
        if estoque[codigo]['quantidade'] >= quantidade:
            estoque[codigo]['quantidade'] -= quantidade
        else:
            print('Não há quantidade suficiente no estoque.')
    else:
        print('Produto não encontrado.')


def relatorio_geral():
    print('Código\tDescrição\tQuantidade')
    for codigo, produto in estoque.items():
        print(f'{codigo}\t{produto["descricao"]}\t{produto["quantidade"]}')


def relatorio_nao_disponiveis():
    print('Código\tDescrição')
    for codigo, produto in estoque.items():
        if produto['quantidade'] == 0:
            print(f'{codigo}\t{produto["descricao"]}')


def salvar_estoque():
    with open('estoque.pkl', 'wb') as arquivo:
        pickle.dump(estoque, arquivo)


def carregar_estoque():
    try:
        with open('estoque.pkl', 'rb') as arquivo:
            estoque.update(pickle.load(arquivo))
    except FileNotFoundError:
        print('Não foi encontrado um arquivo de estoque.')


# Teste do programa
carregar_estoque()
entrada_produto(1, 'Arroz', 5)
entrada_produto(2, 'Feijão', 3)
entrada_produto(1, 'Arroz', 2)
retirada_produto(1, 3)
retirada_produto(2, 5)
relatorio_geral()
relatorio_nao_disponiveis()
salvar_estoque()
