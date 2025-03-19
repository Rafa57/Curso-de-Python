# DICTIONARY COMPREHENSION E SET COMPREHENSION

# product = {
#     'Name': 'Rice',
#     'Price': 4.5,
#     'Category': 'Food'
# }

# # for key, value in product.items():
# #     print(key, value)


# dc = {
#     key: value.upper()
#     if isinstance(value, str) else value
#     for key, value in product.items()
#     if key != 'Category'
# }

# lst = [
#     ('a', 'valor de a'),
#     ('b', 'valor de b'),
#     ('c', 'valor de c'),
# ]

# print(dc)

# st1 = {i ** 2 for i in range(12)}
# print(st1)
# ---------------------------------------------

# ISINSTANCE() - PARA SABER SE UM OBJETO É DE DETERMINADO TIPO
lst1 = [
    'a', 1, 1.1, True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'nome': 'Rafael'},
]

for i in lst1:
    if isinstance(i, list):
        i.append(6)
        print(i)

    if isinstance(i, str):
        i.upper()
        print(i.upper())