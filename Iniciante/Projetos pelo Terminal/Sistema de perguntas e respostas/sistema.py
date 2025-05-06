# Sistema de perguntas e repostas 

qtd_acertos = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2 ?',
        'Opções': ['1','3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5 ?',
        'Opções': ['25', '55', '10', '35'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2 ?',
        'Opções': ['4', '2', '1', '5'],
        'Resposta': '5',
    }
]

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print(end='\n')

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print(end='\n')
    
    escolha = input('Escolha uma opção: ')

    acertou = False
    int_escolha = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        int_escolha = int(escolha)
    
    if int_escolha is not None:
        if int_escolha >= 0 and int_escolha < qtd_opcoes:
            if opcoes[int_escolha] == pergunta['Resposta']:
                acertou = True

        if acertou:
            qtd_acertos += 1
            print('Acertou 👍')
        else:
            print('Errou 😕')
    print(end='\n')

print(f'Você acertou {qtd_acertos} respostas de {len(perguntas)} perguntas 🎉')

