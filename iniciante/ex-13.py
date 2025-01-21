# exercicios com funções
# crie uam função que multiplica todos os argumentos não nomeados recebidos

def multiplication(*args):
    result = 1
    for i in args:
        result *= i

    return result

def even_odd(number): # par e ímpar
    number % 2 == 0

    return 'It is an even number.' if number else 'It is an odd number.'

final_result = multiplication(7, 5)
num_is_even = even_odd(final_result)

print(final_result)
print(num_is_even)