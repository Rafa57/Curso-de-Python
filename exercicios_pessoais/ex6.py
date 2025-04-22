# contar letras e digitos
# texto = input('digite uma frase (pode conter números): ')

def contagem(entrada):
    cont_char = {'letras': 0, 'digitos': 0}
    entrada = entrada.replace(' ', '')

    for char in entrada.lower():
        if char.isalpha():
            cont_char['letras'] += 1
        if char.isdigit():
            cont_char['digitos'] += 1

    return cont_char

# print(contagem(texto))

# remover palavras duplicadas
palavra_duplicada = 'python é top e python é divertido'

def verificar_dupli(palavra):
    frase_final = ''
    palavra = palavra.lower().split()

    for i in palavra:
        if i not in frase_final:
            frase_final += i + ' '

    return frase_final

print(verificar_dupli(palavra_duplicada))
# ------------------------------------------------------

# 3. converter lista de tuplas em dicionário
tuple_list = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]

def convert_to_list(var):
    dictio = {}

    for key, value in var:
        if key not in dictio:
            dictio[key] = [value]
        else:
            dictio[key].append(value)

    return dictio

print(convert_to_list(tuple_list))
# ------------------------------------------------------

# 4. palavras em ordem alfabética invertida por tamanho

