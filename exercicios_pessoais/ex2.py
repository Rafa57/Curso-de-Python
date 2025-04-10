def verify(function):
    result = [num for num in function if (num ** (0.5)) % 2 == 0]
    return result

def pair_num(len) -> list:
    create_lst = [item for item in range(1, len + 1)]
    return create_lst

print(verify(pair_num(100)))

# SOMA DOS ELEMENTOS DE UMA LISTA
lst1 = list(range(6))

def soma(lst):
    total = 0
    for i in lst:
        total += lst[i]

    return total
    
print(soma(lst1))
# -----------------------------------

# ELIMINAR DUPLICATAS MANTENDO A ORDEM
def limpar_lista(lst):
    lista_limpa = []

    for i in lst:
        if i not in lista_limpa:
            lista_limpa.append(i)

    return lista_limpa

lista1 = [1, 2, 2, 3, 1, 4, 3, 4, 5, 6, 7, 8, 7, 7, 2]

print(limpar_lista(lista1))
# --------------------------------------------------

# 