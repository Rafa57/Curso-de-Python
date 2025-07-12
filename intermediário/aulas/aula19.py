# LIST COMPREHENSION EM PYTHON
# List comprehension é uma forma rápida de criar listas a partir de iteráveis.
import pprint

print('list(): ', list(range(12)))

list1 = []
for i in range(12):
    list1.append(i)
print('for: ', list1)

# list comprehension
list2 = [i * 3 for i in range(12)]
print('list comp: ', list2)
#------------------------------------------------

# mapeamento de dados em list comprehension
products = [
    {'name': 'p1', 'price': 21},
    {'name': 'p2', 'price': 15},
    {'name': 'p3', 'price': 34},
    {'name': 'p4', 'price': 120}
]

new_prods = [prod for prod in products]
print(*new_prods, sep='\n')

new_prods = [prod['name'] for prod in products]
print(*new_prods, sep='\n')

new_prods = [
    {'nome': prod['name'], 'preco': prod['price'] * 2}
    for prod in products
    ]
print(new_prods)
print(*new_prods, sep='\n')

# a nova lista deve ter a mesma quantidade de elementos que a lista antiga
new_prods = [
    {**prod, 'price': prod['price'] * 1.05}
    if prod['price'] > 20 else {**prod}
    for prod in products
    ]
print('')
print(*new_prods, sep='\n')
#-------------------------------------------------------

# FILTRO DE DADOS EM LIST COMPREHENSION
def pp(*args):
    pprint.pprint(args, sort_dicts=False, width=50)

# FILTRO
new_lst = [
    {**item, 'price': item['price']}
    for item in products 
    if item['price'] >= 20 and item['price'] <= 100
]

print('')
pp(new_lst)
# ------------------------------------------------------

# LIST COPREHENSION COM MAIS DE UM FOR
lst_1 = []
for x in range(3):
    for y in range(3):
        lst_1.append([x, y])

lst_1 = [
    (x, y) 
    for x in range(1, 4) 
    for y in range(1, 4)
]
pp(*lst_1)

lst_1 = [
    [item for item in 'Rafael']
    for _ in range(3)
]
pp(lst_1)