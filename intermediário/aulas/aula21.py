import sys

# # Generator expression, Iterables e Iterators em Python
# iterable = ['tem', 'atributo', '__iter__']
# # iterator = iterable.__iter__() # tem __iter__ e __next__

# iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # -----------------------------------------------

# # Generator - pausa a iteração

# lista = [n for n in range(10)]
# generator = (n for n in range(10)) # Generator expression
# print(sys.getsizeof(generator)) # Não está salvo na memória, apenas sabe o próximo item de um iterável, pois possui __iter__ e __next__

# print(sys.getsizeof(lista))

# for i in generator:
#     print(i)
# # ----------------------------------------------

# Introdução às Gererator functions em Python
# generator = (n for n in range(12))

def generator(n=0, max=12):
    while True:
        yield n # pausa a execução da função
        n += 1
        
        if n > max:
            return
        
    

gen = generator() # tem __iter__ e __next__
for n in gen:
    print(n)

# yield from

def gen1():
    print('<g1>')
    yield 1
    yield 2
    yield 3
    print('</g1>')

def gen3():
    print('<g3>')
    yield 30
    yield 40
    yield 50
    print('</g3>')

def gen2(gen=None):
    print('<g2>')
    if gen is not None:
        yield from gen
        # yield from gen()
    yield 4
    yield 5
    yield 6
    print('</g2>')

g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for num in g1:
    print(num)
for i in g2:
    print(i)
for i in g3:
    print(i)
