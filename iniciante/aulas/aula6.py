# INTRODUÇÃO AO try/except

numero_str = input('dobrarei o número inteiro digitado: ')

print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')

if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}!!')
else:
    print('Isso não é um número inteiro')

try:
    numero_float = float(numero_str)
    print('Str:', numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}!!')
except:
    print('Isso não é um número')
    
    # pass/... = reserva um espaço e retornam um valor nulo (é usado para continuar sem gerar erros)


# BOAS PRÁTICAS 1
'''
CONSTANTE = não existem no python, porém, por convenção, uma variável scrita em maiúsculo é considerada uma constante

IF COM MUITAS CONDIÇÕES É RUIM

'''

velocidade = 78
local = 121

# constantes
RADAR_1 = 70
LOCAL_1 = 120
RADAR_RANGE = 1

acima_do_limite_radar_1 = velocidade > RADAR_1

passou_no_radar_1 = local >= (LOCAL_1 - RADAR_RANGE) and local <= (LOCAL_1 + RADAR_RANGE)

multado_no_radar_1 = passou_no_radar_1 and acima_do_limite_radar_1

if acima_do_limite_radar_1:
    print('Velocidade do carro acima do limite do radar 1')

if multado_no_radar_1:
    print('Carro multado em radar 1')

if passou_no_radar_1:
    print('Carro passou em radar 1')

# ID
v1 = id('a')
v2 = 'a'
print(v1)
print(id(v2))

# Flags, is, is not e none
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')