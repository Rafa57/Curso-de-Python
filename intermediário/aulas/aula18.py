# FUNÇÃO LAMBDA

array = [14, 28, 21, 42, 35, 67]
array.sort() # Modifica a lista original 
# sorted(array) # cria uma cópia rasa da lista

print(array, '\n')

array_2 = [
    {'produto': 'carro', 'preco': 25000},
    {'produto': 'moto', 'preco': 12000},
    {'produto': 'bike', 'preco': 1300}
]

def ordenate(item):
    return item['produto']

array_2.sort(key=ordenate)
print(array_2, '\n')

def show_list(array):
    for i in array:
        print(i)

array_2.sort(key=lambda item: item['produto']) # não precisa da palavra 'return'
arr1 = sorted(array_2, key=lambda item: item['produto']) # cria uma cópia rasa
arr2 = sorted(array_2, key=lambda item: item['preco'])
print('\n', array_2, '\n')

show_list(arr1)

