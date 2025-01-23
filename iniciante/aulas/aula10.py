# introdução ao desempacotamento
# animais = ['rato', 'pato', 'gato']
# animal1, animal2, animal3 = animais
# print(animal2)

nome1, *_ = ['rafael', 'joão', 'lais'] # underscore (underline) como variável indica que a variável existe, mas não será usada.
print(nome1)

_, _, nome2, *_ = ['rafael', 'joão', 'lais'] # *resto -> ainda retorna uma lista, mesmo que seja vazia.
print(nome2)
print(_)

# tuplas (tuple -> conjunto imutável)
nome = 'maria', 'osvaldo', 'pedro'
nome_1 = ('maria', 'osvaldo', 'pedro')
# nome[2] = 'barril' # gera erro porque os valores não podem ser alterados

lista = ['rato', 'gato', 'pato']
lista = tuple(lista)
print(lista, type(lista))
print(20 * '-')

# enumerate -> enumera iteráveis (índices)
lista = ['rato', 'gato', 'pato']
lista.append('gavião')

for item in enumerate(lista):
    print(item)

for item in enumerate(lista):
    a, b = item # desempacotamento
    print(a, b)
print(20 * '-')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
print(20 * '-')

for tupla in enumerate(lista):
    print('FOR da tupla:')
    for indice in tupla:
        print(f"\t{indice}")
print(20 * '-')