# média
def average_num(lst):
    if not lst:
        return 0
    
    return sum(lst) / len(lst)

def average_sum2(lst):
    total = 0
    for i in lst:
        total += i
    
    return total / len(lst)

print('A média 1 é', average_num([5, 10, 15]))
print('A média 2 é', int(average_num([5, 10, 15])))

# inverter lista

def reverse_list(lst):
    reverse_lst = []
    for i in lst:
        reverse_lst.insert(0, i)

    return reverse_lst

num_lst = [1, 2, 3, 4]
str_lst = ['um', 'dois', 'tres', 'quatro']

print(reverse_list(num_lst))
print(reverse_list(str_lst))

# FizzBuzz
def fizzbuzz(n):

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz(30)

# numeros unicos
def unique_num(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(unique_num([1, 2, 2, 3, 1, 4]))