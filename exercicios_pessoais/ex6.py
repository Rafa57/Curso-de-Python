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