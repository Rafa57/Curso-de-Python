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


def ordenar_palavras(palavras):
    return sorted(palavras, key=lambda x: (-len(x), x[::-1]))

lista = ['maçã', 'banana', 'uva', 'abacaxi', 'pera']
print(ordenar_palavras(lista))
# -------------------------------------------------------------

# Teste de manipulação de arquivos externos
lista2 = {n: n + 1 for n in range(5)}
print(lista2)

open('teste.txt', 'w').write('lista')

with open('teste.txt', 'w') as salvar:
    lista_salva = []
    
    for key, value in lista2.items():
        if key not in lista_salva:
            salvar.write('%s: ' %key)
            salvar.write('%d\n' %value)  