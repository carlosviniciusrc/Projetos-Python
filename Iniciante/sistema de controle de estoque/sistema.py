# Sistema de controle de estoque

import os

# Menu
def menu():
    print('Olá, Seja Bem-Vindo')
    print('Categoria de Produtos:')
    print('1. Alimentos')
    print('2. Bebidas')
    print('3. Limpeza')


# Controle de exibição
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Exibir os valores de entrada
def valores():
    print(f'Produto: {nome_do_produto}')
    print(f'Categoria: {categoria_do_produto.upper()}')
    print(f'Quantidade atual em estoque: {quantidade_atual_no_estoque}')


while True:
    limpar_tela()
    menu()

    try:
        # Entrada de valores 
        nome_do_produto = input('Qual o seu produto: ').upper()
        categoria_do_produto = int(input('Qual a categoria do produto (1/2/3): ').strip().lower())
        quantidade_atual_no_estoque = int(input('Qual a quantidade atual no estoque: '))


        if categoria_do_produto not in [1,2,3]:
            print('Escolha uma opcão de 1 a 3.')
            continue

        # Estoque mínimo de cada categoria
        estoque_alimentos = 80
        estoque_bebidas = 70
        estoque_limpeza = 50

        # Variavel de Solicitação
        solicitar_estoque = 0

        if categoria_do_produto == 1:
            categoria_do_produto = 'Alimentos'
            if quantidade_atual_no_estoque < estoque_alimentos:
                solicitar_estoque = estoque_alimentos - quantidade_atual_no_estoque
                os.system('cls')
                valores()
                print(f'Estoque Mínimo: {estoque_alimentos}')
                print(f'Atenção! Solicitar {solicitar_estoque} unidades de {nome_do_produto} para equipe de compras.', end='\n\n')
            else:
                os.system('cls')
                valores()
                print(f'Estoque Mínimo: {estoque_alimentos}')
                print(f'Não precisa fazer solicitação, pois a {quantidade_atual_no_estoque} está acima do valor mínimo do estoque.', end='\n\n')

        if categoria_do_produto == 2:
            categoria_do_produto = 'Bebidas'
            if quantidade_atual_no_estoque < estoque_bebidas:
                solicitar_estoque = estoque_bebidas - quantidade_atual_no_estoque
                os.system('cls')
                valores()
                print(f'Estoque Mínimo: {estoque_bebidas}')
                print(f'Atenção! Solicitar {solicitar_estoque} unidades de {nome_do_produto} para equipe de compras.', end='\n\n')
            else:
                os.system('cls')
                valores()
                print(f'Estoque Mínimo: {estoque_bebidas}')
                print(f'Não precisa fazer solicitação, pois a {quantidade_atual_no_estoque} está acima do valor mínimo do estoque.', end='\n\n')
        
        if categoria_do_produto == 3:
            categoria_do_produto = 'Limpeza'
            if quantidade_atual_no_estoque < estoque_limpeza:
                solicitar_estoque = estoque_limpeza - quantidade_atual_no_estoque
                os.system('cls')
                categoria_do_produto = 'limpeza'
                valores()
                print(f'Estoque Mínimo: {estoque_limpeza}')
                print(f'Atenção! Solicitar {solicitar_estoque} unidades de {nome_do_produto} para equipe de compras.', end='\n\n')
            else:
                os.system('cls')
                valores()
                print(f'Estoque Mínimo: {estoque_limpeza}')
                print(f'Não precisa fazer solicitação, pois a {quantidade_atual_no_estoque} unidades e está acima do valor mínimo do estoque.', end='\n\n')

        # Saida do programa
        print('Deseja continuar na verificação?')
        saida = input('Digite [S] sim ou [N] não: ').lower()

        if saida == 'n':
            os.system('cls')
            print('Encerrando o Sistema. Até mais!')
            break

    except ValueError:
        print('Digite apenas valores válidos 😕.')
        input('Pressione Enter para continuar...')