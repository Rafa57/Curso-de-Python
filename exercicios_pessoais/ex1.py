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
def palindrome(text):
    text = str(text).lower()
    final_txt = text[::-1]

    if final_txt == text:
        return True
    else:
        return False

print(palindrome('tenet'))
print(palindrome('prime'))


# ORDENAÇÃO BUBBLE SORT
bubble_list = [23, 34, 67, 22, 32, 1, 2, 43]
# bubble_list.sort(reverse=True) # sort modifica a lista

def bubble_sort(array):
    return sorted(array) # cria uma cópia rasa

def reverse_bubble_sort(array):
    return sorted(array, reverse=True)

print(bubble_sort(bubble_list))
print(reverse_bubble_sort(bubble_list))


# NUMEROS PRIMOS EM INTERVALO
def prime_verify(num):
    if num < 2:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def prime_number(n1, n2):
    return [n for n in range(n1, n2 + 1) if prime_verify(n)]

print(prime_number(10, 50))


# CONTAGEM DE CARACTERES
def char_count(iter):
    dictio = {}

    for i in iter:
        if i not in dictio:
            counter = 0
            dictio[i] = counter
        if i in dictio:
            dictio[i] += 1

    return dictio

print(char_count('hight'))