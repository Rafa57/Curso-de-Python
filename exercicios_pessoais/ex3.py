import random

# numero par
def num_par(num):
    if num % 2 == 0:
        return f"{num} é par!"
    else:
        return f"{num} é ímpar"
    
print(num_par(15))

# resolução
def num_par(num):
    return f"{num} é par!" if num % 2 == 0 else f"{num} é ímpar"

# -------------------------------------------

# maior numero de uma lista
lista1 = [random.randint(1, 100) for _ in range(10)]

def greater_num(lista):
    lista.sort()
    return lista[-1]

print(lista1)
print(greater_num(lista1))

# resolução
def greater_num(lista):
    return max(lista)

# -----------------------------------------------

# Frequência de palavras
phrase1 = 'hoje é dia de aprender Python Python é legal'

def word_counter(phrase):
    words = phrase.split()
    counter = {}

    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter

print(word_counter(phrase1))
# ------------------------------------------------

# Validação de cpf
def validation(cpf):

    if len(cpf) < 11:
        return f'CPF({cpf}) é inválido!'
    if not cpf.isdigit():
        return f'CPF({cpf}) é inválido!'
    else:
        return f'CPF({cpf}) é válido!'
    
print(validation("23455673789"))
print(validation("2345567"))
print(validation("2345567asdf"))

# resolução
def validation(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return f'CPF({cpf}) é inválido!'
    return f'CPF({cpf}) é válido!'
