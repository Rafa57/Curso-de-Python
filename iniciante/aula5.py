# INTERPOLAÇÃO BÁSICA DE STRINGS
nome = 'Lalinha'
preco = 123.565346
variavel = '%s, o fanho quer R$ %.2f de indenização.' % (nome, preco)
print(variavel)

# x e X - hexadecimal (ABCDEF0123456789)
print('O hexadecimal de %d é %08x' % (5654, 5654))
print(f'O hexadecimal de 4096 é {4096:08x}')

# FORMATAÇÃO BÁSICA DE STRINGS

valor = 'abc'
print(f'{valor}')
print(f'{valor:_>15}')
print(f'{valor:+<15}')
print(f'{valor:-^15}')
print(f'{1267.22344143:0=+10,.2f}')


# FATIAMENTO DE STRING
var = '\noh, the light'
print(var[::-1])
print(len(var))

