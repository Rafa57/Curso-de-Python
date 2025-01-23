lista = [[1,2,3], [4,5,6], [7,8,9]]
lista.append([10,11,12])

indices = range(len(lista))
for i in indices:
    print(i, lista[i])

# minha solução
i = 0
while i < len(lista):
    print(i, lista[i])
    i += 1