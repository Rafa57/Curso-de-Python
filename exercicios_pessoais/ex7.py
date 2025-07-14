# somador de número pares
try:

    def input_lst():
        number_lst = []
        counter = 1

        while counter <= 10:
            number_lst.append(int(input(f"Digite o {counter}º número: ")))
            counter += 1

        return number_lst

    def sum_lst(lst):
        sum_num = 0
        for i in lst:
            if i % 2 == 0:
                sum_num += i
        
        return sum_num
    
    number_lst = input_lst()

    print(number_lst)
    print(sum_lst(number_lst))

except ValueError:
    print('Entrada inválida! Digite apenas números inteiros.')

# Frequência de caracteres

def count(txt):
    char_list = {}

    for c in txt:
        if c not in char_list:
            char_list[c] = 1
        else:
            char_list[c] += 1
            
    return char_list

txt = "banana"
print(count(txt))

# Verificar palíndromo
import unicodedata
import re

def palindrome(txt):
    clean_space = ''

    for i in txt:
        if i.isalpha():
            clean_space += i.lower()

    clean_special = unicodedata.normalize('NFD', clean_space)
    clean_txt = re.sub(r"[\u0300-\u036f]", '', clean_special)
    rvs_txt = clean_txt[::-1]
    
    if clean_txt == rvs_txt:
        return "é palíndromo"
    else:
        return "não é palíndromo"
    
print(palindrome("Socorram-me, subi no ônibus em Marrocos"))