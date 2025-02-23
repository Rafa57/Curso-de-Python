# LIST COMPREHENSION EM PYTHON
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

# print('list(): ', list(range(12)))

# list1 = []
# for i in range(12):
#     list1.append(i)
# print('for: ', list1)

# # list comprehension
# list2 = [i * 3 for i in range(12)]
# print('list comp: ', list2)

#------------------------------------------------

# mapeamento de dados em list comprehension
products = [
    {'name': 'p1', 'price': 21},
    {'name': 'p2', 'price': 15},
    {'name': 'p3', 'price': 34}
]

# new_prods = [prod for prod in products]
# print(*new_prods, sep='\n')

# new_prods = [prod['name'] for prod in products]
# print(*new_prods, sep='\n')

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
print('\n')
print(*new_prods, sep='\n')
