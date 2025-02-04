# SETS - Conjuntos em Python (tipo set)

s1 = set() # set vazio
s2 = {'Rafael', 1, 2, 3} # set com dados
print(s1, s2)

# set elimina valores duplicados automaticamente
conj = {1, 2, 3, 5, 5, 5, 6, 6, 8, 9, 0, 9, 9, 8} 
print(conj)

lista1 = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5]
set1 = set(lista1)
lista2 = list(set1)

# sets não aceitam valores mutáveis, (porém um set é mutável)
# set2 = {1, 2, 3, [1, 2, 3]} # gera erro

# set não garante a ordem
set3 = set("Lais") 
set4 = {1, 2, 3}
print(lista2)
print(set3)

# sets não tem índice
# print(set[0]) 

# sets são iteráveis (for, in, not in)
print(5 not in set4) 
for numero in set4:
    print(numero)

# MÉTODOS ÚTEIS
# add, update, clear, discard

conjunto1 = set()

# add(imutável) -> adiciona um dado imutável
conjunto1.add('Lais') 
conjunto1.add(4)
print(conjunto1)

# update(iterável) -> adiciona cada dado do iterável separadamente
conjunto1.update((1, 2, 3), 'byte') # aceita mais de 1 parâmetro
print(conjunto1)

# clear() -> limpa todo o set
# conjunto1.clear() 
print(conjunto1)

# discard(dado) -> deleta o dado indicado (como set não tem índice, o dado inteiro deve ser passado)
conjunto1.discard('Lais')
print(conjunto1)

# OPERADORES IMPORTANTES PARA O TIPO SET

num1 = {1, 2, 3}
num2 = {2, 3, 4}

# union ( | ) -> une os sets
num3 = num1 | num2
print(num3) # descarta as repetições

# intersection ( & ) -> interseccção entre os sets
num3 = num1 & num2
print(num3)

# diferença ( - ) -> dados específicos do set da esquerda
num3 = num1 - num2 # a ordem importa
print(num3)

# diferença simétrica ( ^ ) -> dados especificos de cada set
num3 = num1 ^ num2 # a ordem não importa
print(num3)

# EXEMPLO DE USO
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 's' in letras:
        print('Saiu')
        break

    print(letras)