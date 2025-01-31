# métodos uteis dos dicionários em Python

import copy

lang = {
    'name': 'Python',
    'cathegory': "Code",
    'age': 40,
    'list': [12, 23, 34]
}

# print(len(book)) # tamanho do dicionário

# print(book.keys()) # retorna as chaves

# print(book.values()) # retorna os valores

# print(book.items()) # retorna as chaves e o valores dentro de tuplas (key, value)

# book.setdefault('age', 56) # adiciona a chave : valor se ela não existir
# print(book['age'])

# shalow copy -> cópia rasa
# book_2 = book_1.copy() # copia os valores imutáveis (não copia listas internas)

# book_2 = copy.copy(book_1) # usando o módulo copy (também é uma cópia rasa)

# book_2 = copy.deepcopy(book_1) # copia os subníveis também (listas internas)

# book_2['age'] = 78
# print(book_1)
# print(book_2)
# book_2['list'][2] = [56, 67, 78] # não copia, apenas aponta para a mesma lista em book_1
# print(book_1)
# print(book_2)

# for value in book.values():
#     print(value)

# for key, value in book.items():
#     print(f'{key}: {value}')

# get
print(lang.get('name')) # retorna o valor da chave (retorna None como padrão)

print(lang.get('height', 'not found')) # o valor padrão pode ser mudado

# pop
# print(book1)
# del_age = book1.pop('age') # apaga um item com a chave indicada
# print(book1)

# popitem
print(lang)
del_list = lang.popitem() # apaga a ultima chave do dicionario
print(del_list) # retorna o par chave:valor removido
print(lang)

# Update
lang.update({
    'name': 'PHP',
    'area': 'back-end'
}) # atualiza o dicionário (adicionar, atualizar)
print(lang)

lang.update(name='js', area='front-end') # segunda forma
print(lang)

form_3 = ('name', 'java'), ('area', 'back-end') # deixar uma virgula no final da tupla se tiver somente uma ( ('key', 'value'), )
lang.update(form_3)
print(lang)

form3_list = [['name', 'Kotlin'], ['area', 'android']]
lang.update(form3_list)
print(lang)
