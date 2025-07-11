
from copy import deepcopy
from operator import itemgetter
from data.ex18_db import products

print(*products, sep="\n")
print()
print("----------------------------------------")

# Aumente os preços dos produtos a seguir em 10%
# gere novos produtos por deep copy (cópia profunda)

def calc_tax(tax):
    new_prods = deepcopy(products)

    for prod in new_prods:
        prod["price"] = round(prod["price"] * tax, 2)
    
    return new_prods

print(*calc_tax(1.1), sep="\n")
print()


# ordene os produtos por nome decressente
# gere produtos ordenados por nome por deep copy

def increased_sort():
    increased_lst = sorted(products, key=itemgetter("name"))
    return increased_lst[::-1]

print(*increased_sort(), sep="\n")
print()


# oderene os produtos por preço crescente
# gere produtos ordenados por preço por deep copy

def decreased_sort():
    return deepcopy(sorted(products, key=itemgetter('price')))

print(*decreased_sort(), sep="\n")
print("----------------------------------------")
print()

# resolução

novos_produtos = [
   {**n, 'price': round(n['price'] * 1.1, 2)} 
   for n in deepcopy(products)
]

print(*novos_produtos, sep="\n")
print()

produtos_por_nome = sorted(
    deepcopy(products),
    key=lambda n: n['name'],
    reverse=True
)

print(*produtos_por_nome, sep='\n')
print()

produtos_por_valor = sorted(
    deepcopy(products),
    key=lambda p: p['price'],
)

print(*produtos_por_valor, sep='\n')