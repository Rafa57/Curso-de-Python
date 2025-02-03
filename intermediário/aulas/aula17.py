# SETS - Conjuntos em Python (tipo set)

# s1 = set() # set vazio
# s2 = {'Rafael', 1, 2, 3} # set com dados
# print(s1, s2)

# conj = {1, 2, 3, 5, 5, 5, 6, 6, 8, 9, 0, 9, 9, 8} # set elimina valores duplicados automaticamente
# print(conj)

lista1 = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5]
set1 = set(lista1)
lista2 = list(set1)
# set2 = {1, 2, 3, [1, 2, 3]} # set não aceita valores mutáveis, (porém o set é mutável)
set3 = set("Lais") # set não garante a ordem
set4 = {1, 2, 3}

print(lista2)
# print(set2)
print(set3)
# print(set[0]) # set não tem índice

print(5 not in set4) # set são iteráveis (for, in, not in)
for numero in set4:
    print(numero)