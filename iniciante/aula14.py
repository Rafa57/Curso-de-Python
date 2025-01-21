# HIGHER ORDER FUNCTIONS -> Funções que podem receber e/ou retornar outras funções
# FIRST-CLASS FUNCTIONS - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

def greeting(person, msg):
    return f'Hi {person}, {msg}'

def execute(function, *args):
    return function(*args)
 
print(execute(greeting, 'Lais', 'good afternoon.'))


# teste com lista (código pessoal)-----------------------
def add(*args):
    lista = []
    lista.extend(args) # Itera sobre os elementos de args e os adiciona individualmente à lista.
    return lista

def executar(function, *args):
    return function(*args)

print(executar(add, 'nome', 'dia', 'mes', 'ano'))
# -------------------------------------------------------