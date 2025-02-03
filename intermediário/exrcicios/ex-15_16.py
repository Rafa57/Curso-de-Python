# SISTEMA DE PERGUNTAS E RESPOSTAS

questions = [
    {
        'Pergunta': 'Quanto é 12 + 24?',
        'Opções': ['32', '12', '36', '40', '42'],
        'Resposta': '36'
    },
    {
        'Pergunta': 'Quanto é 6 * 5?',
        'Opções': ['26', '45', '30', '65', '36'],
        'Resposta': '30'
    },
    {
        'Pergunta': 'Quanto é 81 / 9?',
        'Opções': ['3', '19', '72', '90', '9'],
        'Resposta': '9'
    }
]

# def answer(question):
#     def quest(aswr):
#         options = questions[question].get('Opções')
#         correct = questions[question].get('Resposta')

#         if aswr not in options:
#            return 'Opção inválida.\n'
#         if aswr != correct:
#             return 'Resposta errada.\n'
#         else:
#             return 'Certa resposta.\n'

#     return quest

# def user_answer():
#     quest_1 = answer(0)
#     quest_2 = answer(1)
#     quest_3 = answer(2)

#     print(questions[0].get('Pergunta'))
#     for i in questions[0].get('Opções'):
#         print(i)
#     print(quest_1(input('Digite a resposta: ')))

#     print(questions[1].get('Pergunta'))
#     for i in questions[1].get('Opções'):
#         print(i)
#     print(quest_2(input('Digite a resposta: ')))

#     print(questions[2].get('Pergunta'))
#     for i in questions[2].get('Opções'):
#         print(i)
#     print(quest_3(input('Digite a resposta: ')))

# user_answer()

# RESOLUÇÃO

qtd_acertos = 0
qtd_erros = 0

for pergunta in questions:

    print(pergunta['Pergunta'])
    opcoes = pergunta['Opções']
    
    for i, opcao in enumerate(opcoes):
        # letra = chr(65 + i) # usa o código ASCII (A = 65)
        print(f'{i}) {opcao}')
        
    resp_usuario = input('Resposta: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if resp_usuario.isdigit():
        escolha_int = int(resp_usuario)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Certa resposta!\n')
    else:
        qtd_erros += 1
        print("Resposta errada!\n")

print(f'Quantidade de acertos: {qtd_acertos}')
print(f'Quantidade de erros: {qtd_erros}')