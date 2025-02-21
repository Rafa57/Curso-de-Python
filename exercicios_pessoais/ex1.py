# SEQUENCIA DE FIBONACCI
def fibonnaci(num):
    if num <= 0:
        return 'numero invalido'
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonnaci(num - 1) + fibonnaci(num - 2)

print(fibonnaci(10))


# PALÍNDROMO

def palindromo(text):
    text = str(text).lower()
    final_txt = text[::-1]

    if final_txt == text:
        return True
    else:
        return False

print(palindromo('tenet'))
print(palindromo('prime'))


# ORDENAÇÃO BUBBLE SORT

bubble_list = [23, 34, 67, 22, 32, 1, 2, 43]
# bubble_list.sort(reverse=True) # sort modifica a lista
# print(bubble_list)

def bubble_sort(array):
    return sorted(array) # cria uma cópia rasa

def reverse_bubble_sort(array):
    return sorted(array, reverse=True)

print(bubble_sort(bubble_list))
print(reverse_bubble_sort(bubble_list))


# NUMEROS PRIMOS EM INTERVALO

def prime_number(num1, num2):
    number_list = []

    while num1 <= num2:
        if num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0:
            number_list.append(num1)

        num1 += 1

    return number_list

print(prime_number(10, 50))