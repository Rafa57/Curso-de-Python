# loop for

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'-{letra}-'
    print(letra)

print(novo_texto)

# for + range
# range -> range(start, stop, step)

numeros = range(3, 15, 3)

for numero in numeros:
    print(numero)


# COMO FUNCIONA O LOOP FOR
'''Iterável -> str, range, etc. (__iter__)
   Iterador -> quem sabe entregar um valor por vez
   next -> me entregue o próximo valor
   iter -> me entregue seu iterador
'''

texto = iter('Rafael') # __iter__()

print(texto.__next__())
print(next(texto)) # é a mesma função (__next__())
print(next(texto))
print(texto.__next__())

# for letra(iterador) in texto(iterável)
texto = "Laís" # iterável
iterador = iter(texto) # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in texto: # é igual ao while acima
    print(letra)


for i in range(11):
    if i == 3:
        print('i é 3, pulando...')
        continue
    
    if i == 9:
        print('i é 9, o else não executará')
        continue

    for j in range(1, 6):
        print(i, j)

else:
    print('For completo com sucesso!')