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

for pergunta in questions:
    print(pergunta['Pergunta'])

    for i, opcao in enumerate(pergunta['Opções']):
        # letra = chr(65 + i) # usa o código ASCII (A = 65)
        print(f'{i}) {opcao}')
        
    resp_certa = pergunta['Resposta']
    resp_usuario = input('Resposta: ')

    if int(resp_usuario) < 0 and int(resp_certa) > len(pergunta):
        print('Opção inválida.\n')
    elif resp_usuario != resp_certa:
         print('Resposta errada.\n')
    else:
        print('Resposta certa.\n')
