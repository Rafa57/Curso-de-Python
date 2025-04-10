# DICTIONARY COMPREHENSION E SET COMPREHENSION

product = {
    'Name': 'Rice',
    'Price': 4.5,
    'Category': 'Food'
}

# for key, value in product.items():
#     print(key, value)


dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key != 'Category'
}

lst = [
    ('a', 'valor de a'),
    ('b', 'valor de b'),
    ('c', 'valor de c'),
]

print(dc)

st1 = {i ** 2 for i in range(12)}
print(st1)
# ---------------------------------------------

# ISINSTANCE() - PARA SABER SE UM OBJETO É DE DETERMINADO TIPO
lst1 = [
    'a', 1, 1.1, True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'nome': 'Rafael'},
]

for i in lst1:
    if isinstance(i, list):
        i.append(i[:4])
        print(i)

    if isinstance(i, str):
        print(i.upper())

    if isinstance(i, dict):
        print(i['nome'])

# VALORES Truthy e Falsy, Tipos Mutáveis e imutáveis
# Mutáveis [] {} set()
# Imutáveis () ""  0 0.0 None False range(0, 10)

lista = [] # FALSY
dicionario = {} # FALSY
conjunto = set() # FALSY
tupla = () # FALSY
string = '' # FALSY
inteiro = 0 # FALSY
flutuante = 0.0 # FALSY
nada = None # FALSY
falso = False # FALSY
intervalo = range(0) # FALSY
# --------------------------------------------

# dir, hassttr e getattr em Python
nome = 'Lais Thaina'
metodo = 'strip'


if hasattr(nome, 'upper'):
    print('Existe o metodo upper')
    print(nome.upper())

if hasattr(nome, 'lower'):
    print('Tem lower')
    print(getattr(nome, metodo)())