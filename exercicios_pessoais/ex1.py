# SEQUENCIA DE FIBONACCI

def fibonacci(num):
    lista_fibo = []
    f1, f2 = 0, 1

    for _ in range(num):
        lista_fibo.append(f1)
        f1, f2 = f2, f1 + f2
        
    return lista_fibo

print(*fibonacci(10))

# def fibonacci(num):
#     lista_fibo = []
#     f1 = 0
#     f2 = 1

#     for _ in range(num):
#         lista_fibo.append(f1)
#         f1 = f2
#         f2 = f1 + f2
        
#     return lista_fibo

# print(*fibonacci(10))
# -----------------------------------------------

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
# -------------------------------------------

# ORDENAÇÃO BUBBLE SORT

bubble_list = [23, 34, 67, 22, 32, 1, 2, 43]
# bubble_list.sort(reverse=True) # sort modifica a lista

def bubble_sort(lst) -> list:
    return sorted(lst) # cria uma cópia rasa

def reverse_bubble_sort(lst):
    return sorted(lst, reverse=True)

print(bubble_sort(bubble_list))
print(reverse_bubble_sort(bubble_list))
# ------------------------------------------------

# NUMEROS PRIMOS EM INTERVALO

def prime_verify(num):
    if num < 2:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def prime_number(n1, n2) -> list:
    return [n for n in range(n1, n2 + 1) if prime_verify(n)]

print(prime_number(10, 50))
# -------------------------------------------------

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

print(char_count('banana'))