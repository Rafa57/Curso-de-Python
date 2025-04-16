# 1: Cadastro de usuário
user = {
    'Name': 'David',
    'Age': 34,
    'City': 'Toronto'
}

def show_msg(dictionary):
    return f'{dictionary["Name"]} is {dictionary["Age"]} years old and live in {dictionary["City"]}.'

print(show_msg(user))
#----------------------------------------------

# 2: Contando os elementos
fruits = {
    'Banana': 10,
    'Apple': 5,
    'Orange': 9
}

def counting(dictionary):
    
    if 'Banana' in dictionary:
        dictionary['Banana'] = dictionary.get('Banana', 0) + 5
    if 'Apple' in dictionary:
        dictionary['Apple'] = max(0, dictionary.get('Apple', 0) - 2)

    return dictionary

print(counting(fruits))

#---------------------------------------------

# 3: Frequência de letras

def count_letters(s):
    count = {}
    s = s.replace(' ', '').lower()

    for i in s:
        # count[i] = count.get(i, 0) + 1    
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    return count

print(count_letters("Banana"))
#--------------------------------------------

# 4: Atualição de estoque
stock1 = {'apple': 30, 'banana': 23, 'pear': 45}
stock2 = {'banana': 54, 'apple': 34, 'pineapple': 21}

def sum_dictio(dictio1, dictio2):
    added_dictio = {}

    for key in dictio1:
        added_dictio[key] = dictio1.get(key, 0)

    for key in dictio2:
        if key not in added_dictio:
            added_dictio[key] = dictio2.get(key, 0)
        else:
            added_dictio[key] += dictio2.get(key, 0)

    return added_dictio

print(sum_dictio(stock1, stock2))

# resolução
from collections import defaultdict

def sum_dictio(dict1, dict2):
    combined = defaultdict(int)
    
    for d in (dict1, dict2):
        for key, value in d.items():
            combined[key] += value
            
    return dict(combined)
#------------------------------------------------