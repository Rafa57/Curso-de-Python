# INTRODUÇÃO AO try/except

numero_str = input('dobrarei o número inteiro digitado: ')

# print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}!!')
# else:
#     print('Isso não é um número inteiro')

try:
    numero_float = float(numero_str)
    print('Str:', numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}!!')
except:
    print('Isso não é um número')
    
    # pass/... = reserva um espaço e retornam um valor nulo (é usado para continuar sem gerar erros)