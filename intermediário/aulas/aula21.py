import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['tem', 'atributo', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next__

iterator = iter(iterable) # tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
# -----------------------------------------------

# Generator - pausa a iteração

lista = [n for n in range(10)]
generator = (n for n in range(10)) # Generator expression
print(sys.getsizeof(generator)) # Não está salvo na memória, apenas sabe o próximo item de um iterável, pois possui __iter__ e __next__

print(sys.getsizeof(lista))

for i in generator:
    print(i)
# ----------------------------------------------

# Introdu