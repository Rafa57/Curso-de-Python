# didionários (tipo dict)

dic_1 = [
    {
        'Nome': 'Rafael',
        'Idade': 29,
        'Sexo': 'M',
        'Profissão': [
            {'formação': 'Desenvolvedor', 'area': 'front-end'},
            {'formação': 'não tem', 'area': 'design gráfico'}
        ]
    },
    {
        'Nome': 'Laís',
        'Idade': 29,
        'Sexo': 'F',
        'Profissão': [
            {'formação': 'Designer', 'area': 'design gráfico'}
        ]
    }
]

person = dict(name='Rafael', age=29, sex='M', job='Dev')

person_2 = {
        'Nome': 'Rafael',
        'Idade': 29,
        'Sexo': 'M',
        'Profissão': [
            {'formação': 'Desenvolvedor', 'area': 'front-end'},
            {'formação': 'não tem', 'area': 'design gráfico'}
        ]
    }

# print(dic_1[0]['Profissão'])
# print(person)

for chave in person_2:
    print(chave, person_2[chave])

for chave in dic_1[1]:
    print(chave, dic_1[1][chave])

# MANIPULANDO AS CHAVES E VALORES EM DICIONÁRIOS

person_3 = {} # as chaves devem ser tipos imutáveis (int, float, strings, tuplas e valores booleanos.)

# definindo chaves e valores de forma dinâmica

key = 'name' # dessa forma, só é necessário alterar a variável
person_3[key] = 'Rafael'

person_3["age"] = 29 # dessa forma, a alteração deve ser feita em todos os lugares que referenciam essa chave

print(person_3)
print(person_3[key], person_3['age'])

del person_3['age']
print(person_3)

print(person_3.get('surname', None)) # retorna None se a chave não existir (padrão)

if person_3.get('surname') is None:
    print('the key dont exist.')
else:
    print(person_3['surname'])

print(person_3['sobrenome'])
