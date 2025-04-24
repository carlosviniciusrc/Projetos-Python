# Calculadora 

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('== Seja Bem-Vindo ==')
    print('Selecione a operação desejada:')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

def operador(func, x, y):
    return func(x, y)

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    return a / b

if __name__ == "__main__":
    while True:
        limpar_tela()
        menu()

        try:
            entrada = int(input('Selecione a operação desejada (1/2/3/4/5): '))

            if entrada == 5:
                print('Encerrando calculadora. Até mais!')
                break

            if entrada not in [1, 2, 3, 4]:
                print('Selecione uma opção válida.')
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if entrada == 1:
                print(f'A soma de {num1} + {num2} = {soma(num1, num2)}')
            elif entrada == 2:
                print(f'A subtração de {num1} - {num2} = {sub(num1, num2)}')
            elif entrada == 3:
                print(f'A multiplicação de {num1} * {num2} = {multi(num1, num2)}')
            elif entrada == 4:
                if num2 == 0:
                    print('Erro ❌: Divisão por zero não é permitida.')
                    continue
                print(f'A divisão de {num1} / {num2} = {divi(num1, num2)}')

            saida = input('Digite [s] para sair ou [c] para continuar: ').lower()
            if saida == 's':
                print('Encerrando calculadora. Até mais!')
                break

        except ValueError:
            print('Digite apenas valores válidos 😕.')
            input('Pressione Enter para continuar...')



