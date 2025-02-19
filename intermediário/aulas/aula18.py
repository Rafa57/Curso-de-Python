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

# ----------------------------------------------

def execute(function, *args):
    return function(*args)

def sum_num(x, y):
    return x + y

def create_multi(multi):
    def multiplicate(number):
        return number * multi
    return multiplicate

print(execute(lambda x, y: x + y, 5, 6))

dulpicate = execute(lambda m: lambda n: m * n, 2)
print(dulpicate(2))

print(execute(lambda *args: sum(args), 1, 2, 3, 4, 5))

# ---------------------------------------------
# EMPACOTAMENTO E DESEMPACOTAMENTO
# args e kwargs - keyword arguments (argumentos nomeados)

a, b = 1, 2
a, b = b, a # empacotamento
print(a, b)

pessoa = {
    'name:': 'Rafael',
    'surname:': 'Santos'
}

a, b = pessoa.values() # retorna os valores das chaves
print(a, b)

a, b = pessoa.items() # retorna os itens (chave: valor) em tuplas
print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for a, b in pessoa.items():
    print(a, b)

addres = {
    'street:': 'Marcílio dias',
    'number:': 98,
    'neighborhood:': 'Gera bala'
}

complete_person = {**pessoa, 'age:': 29, 'height:': 1.75, **addres} # para desempacotar um dicionário é usado **
print(complete_person)

def show_named_arguments(*args, **kwargs): # os argumentos nomeados ficam armazenados somente em **kwargs
    print(*args)

    for key, value in kwargs.items():
        print(key, value)

show_named_arguments("costumer:", name='Lais', age=28)
show_named_arguments(**complete_person) # dicionários podem ser passados como argumentos nomeados (kwargs)
