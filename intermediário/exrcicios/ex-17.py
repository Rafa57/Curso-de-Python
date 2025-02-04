# CRIE UMA FUNÇÃO QUE ENCONTRA O PRIMEIRO DUPLICADO CONSIDERANDO O SEGUNDO NÚMERO COMO A FUPLICAÇÃO. RETORNE A DUPLICAÇÃO CONSIDERADA

''' 
REQUISITOS:
    A ordem do número duplicado é considerada a partir da segunda ocorrencia do número, ou seja, o número duplicado em si.   
'''

bidimensional_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [19, 72, 32, 41, 32, 32, 32, 5, 34, 56],
    [11, 32, 53, 48, 59, 60, 9, 9, 9, 102],
    [1, 2, 3, 4, 5, 8, 8, 8, 8, 15],
    [1, 2, 3, 7, 5, 7, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 5, 5, 8, 9, 102],
    [1, 2, 3, 2, 1, 2, 5, 2, 9, 10],
    [1, 2, 14, 4, 14, 2, 14, 8, 9, 102]
]

def repetitions():
    for i in bidimensional_list:
        checked = set()

        for value in i:

            if value not in checked:
                counting = i.count(value)

                if counting > 1:
                    print(f'Linha: {i}\nValor: {value}\nRepetições: {counting}\n')

            checked.add(value)

repetitions()