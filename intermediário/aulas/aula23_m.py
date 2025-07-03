
nome = __name__
print(nome)

def mostrar_lista(lista):
    lista_antiga = ['Claudia', 'Nadart']
    if lista not in lista_antiga:
        for i in lista:
            lista_antiga.append(i)
    return lista_antiga