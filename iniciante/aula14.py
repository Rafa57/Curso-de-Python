# HIGHER ORDER FUNCTIONS (first class functions)

# def greeting(person, msg):
#     return f'Hi {person}, {msg}'

# def execute(function, *args):
#     return function(*args)
 
# print(execute(greeting, 'Lais', 'good afternoon.'))

def add(*args):
    lista = []
    lista.extend(args) # Itera sobre os elementos de args e os adiciona individualmente à lista.
    return lista

def executar(function, *args):
    return function(*args)

print(executar(add, 'nome', 'dia', 'mes', 'ano'))