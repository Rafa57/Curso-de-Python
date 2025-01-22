# # HIGHER ORDER FUNCTIONS -> Funções que podem receber e/ou retornar outras funções
# # FIRST-CLASS FUNCTIONS - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

# def greeting(person, msg):
#     return f'Hi {person}, {msg}'

# def execute(function, *args):
#     return function(*args)
 
# print(execute(greeting, 'Lais', 'good afternoon.'))

# # teste com lista (código pessoal)-----------------------
# lista = []

# def add(*args):
#     lista.extend(args) # Itera sobre os elementos de args e os adiciona individualmente à lista.
#     return lista

# def executar(function, *args):
#     return function(*args)

# print(executar(add, 'nome', 'dia', 'mes', 'ano'))
# # -------------------------------------------------------

# CLOSURE E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES

def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}'
    return greet
    

speak_gd_morning = create_greeting('Bom dia')
speak_gd_afternoon = create_greeting('Boa tarde')

for name in ['lais', 'Rafael', 'joão']:
    print(speak_gd_morning(name))
    print(speak_gd_afternoon(name))