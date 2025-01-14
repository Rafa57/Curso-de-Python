# listas
# listas são um tipo de dado mutável

lista = [123, 'avião', 1.2, True, ['casa', 'cabana', 'casebre']]
lista[1] = 'carro'
print(lista[1].upper()) # .upper() só pode ser usado em string

moradias = lista[4]
print(moradias)

lista_vazia = [] # lista vazia = falsy
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(type(matriz))

# CRUD (Creat - Read - Update - Delete)

lista_2 = [12, 34, 56, 78, 23] # Creat

print(lista_2) # Read

valor_lista = lista_2[3] # Update
print(valor_lista)

del lista_2[3] # Delete

# .append() -> adiciona itens no final da lista
lista_2.append(59) 
print(lista_2)

# .pop() -> remove o ultimo item da lista
lista_2.pop() 
ultimo_valor = lista_2.pop()
print(lista_2, 'Removido:', ultimo_valor)

# del -> deleta o item no índice indicado
lista_2.append('rato')
print(lista_2)
del lista_2[-1] 
print(lista_2)

# .insert(indice, valor) -> adiciona o valor no índice indicado
lista_2.insert(1, 25) # se o indice indicado for maior que o tamanho da lista, o valor será adicionado no final da lista (não gera erro, mas deveria)
print(lista_2)

# .clear() -> limpa a lista
lista_2.clear()
print(lista_2)

# + -> concatena listas 
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)

# extend -> Estende a lista
lista_d = lista_a.extend(lista_b) # Retorna None porque o extend() modifica o argumento diretamente
print(lista_a)

# CUIDADOS COM DADOS MUTÁVEIS
caixa_1 = ['faca', True, 12, 1.2] # valores imutáveis
caixa_2 = caixa_1
caixa_1[0] = 'Knife'
# ambas as variáveis apontam para um mesmo valor na memória

print(caixa_2)

#copy()
caixa_1 = ['faca', True, 12, 1.2] # valores imutáveis
caixa_2 = caixa_1.copy()
caixa_1[0] = 'Knife'

print(caixa_1, 'original')
print(caixa_2, 'copia')

# FOR IN COM LISTAS

lista = ['cabra', 'Vaca', 'cachorro']

for animal in lista:
    print(animal, type(animal))
