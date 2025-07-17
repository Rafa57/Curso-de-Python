# contar vogais em uma frase
import unicodedata
import re

def clean_txt(txt):
    txt = unicodedata.normalize('NFD', txt)
    txt = re.sub(r'[^\w\s]','', txt).replace(' ','') # retira espaços e caracteres especiais
    txt = re.sub(r"[\u0300-\u036f]",'', txt).lower() # retira os acentos

    return txt

def vogal_filter(txt):
    vogal_count = 0
    for i in txt:
        if i in 'aeiou':
            vogal_count += 1
    return vogal_count

phrase = "Olá, tudo bem?"
print(f'A frase "{phrase}" tem {vogal_filter(clean_txt(phrase))} vogais')

# Dicinário de quadrados
# def squared(lst):
#     new_dict = {}
#     for i in lst:
#         if isinstance(i, int):
#             new_dict[i] = i ** 2
#         else:
#             print('Digite somente números inteiros')
#             return
#     return new_dict

def squared(lst):
    return {i: i**2 for i in lst if isinstance(i, int)}

num_list = [2, 3, 5]
print(squared(num_list))

# Maior palavra de uma frase
def greater_word(txt):
    txt = txt.split()
    greater = ''
    for w in txt:
        if len(w) > len(greater):
            greater = w
    return f'A palavra "{greater}" é a maior e tem {len(greater)} letras.'

print(greater_word("Programar é uma arte divertida"))

# validador de senha simples

def num_verify(password):
    return True if re.search(r'\d', password) else False
    # return bool(re.search(r'\d', password)) # outra opção

def upper_verify(password):
    return any(c.isupper() for c in password) # VERIFICA CADA ITEM DO ITERÁVEL E RETORNA TRUE SE TIVER PELO MENOS UMA LETRA MAIÚSCULA

def lower_verify(password):
    return any(c.islower() for c in password)

def validation(password):
    valid_password = 'Teste123'

    if len(password) < 8:
        return 'A senha deve conter pelo menos 8 caracteres'
    if not num_verify(password):
        return 'A senha deve conter pelo menos um número'
    if not upper_verify(password):
        return 'A senha deve conter pelo menos uma letra maiúscula'
    if not lower_verify(password):
        return 'A senha deve conter pelo menos uma letra minúscula'
    if password != valid_password:
        return 'A senha é diferente da senha válida'
    else:
        return 'Senha válida!'
    
print(validation('Teste'))
print(validation('Testeumdoistres'))
print(validation('teste123'))
print(validation('TESTE123'))
print(validation('tesTe123'))
print(validation('Teste123'))