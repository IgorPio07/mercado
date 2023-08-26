from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_flot_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('===============================')
    print('=====Bem-Vindo ao Mercado====== ')
    print('===============================')

    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    match opcao:
        case 1:
            cadastrar_produto()
        case 2:
            listar_produto()
        case 3:
            comprar_produto()
        case 4:
            visualizar_carrinho()
        case 5:
            fechar_pedido()
        case 6:
            print('Volte Sempre!')
            sleep(2)
            exit(0)
        case _:
            print('Operacao Invalida!')
            sleep(1)
            menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto:')
    print('====================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o valor do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O Produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos:')
        print('---------------------------')
        for produto in produtos:
            print(produto)
            print('-----------------------')
            sleep(0.8)
    else:
        print('Ainda não exitem produtos cadastrados')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho:')
        print('-------------------------------------------------------------')
        print('Produtos Disponíveis: ')
        for produto in produtos:
            print(produto)
            print('--------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrihno: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {item[produto]} unidades no carrinho!')
                        tem_no_carrihno = True
                        sleep(2)
                        menu()
                if not tem_no_carrihno:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrihno')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(1)
                menu()
        else:
            print(f'O produto com o código {codigo} não está cadastrado no sistema')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print(f'Produtos no carrinho: ')

        for items in carrinho:
            for dados in items.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('---------------------------')
                sleep(1)
    else:
        print(f'Ainda não existem produtos no carrinho')
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho:')
        print('---------------------')
        for item in carrinho:
            for dados in item.items():  # Retorna todos os itens da forma -> chave: valor
                print(dados[0])  # Imprime a chave de cada item, no caso o Produto __str__
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------------------')
                sleep(1)
        print(f'A sua fatura é {formata_flot_str_moeda(valor_total)}')
        print(f'Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('O carrinho está vazio')
        sleep(2)
        menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
