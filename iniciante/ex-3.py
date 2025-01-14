num_1 = input('Insert a number: ')
num_2 = input('Insert another number: ')

if num_1 > num_2:
    print(f'The value 1 = {num_1} is bigger than value 2 = {num_2}')
elif num_1 < num_2:
    print(f'The value 2 = {num_2} is bigger than value 1 = {num_1}')
else:
    print(f'The value 1 = {num_1} is equal to value 2 = {num_2}')