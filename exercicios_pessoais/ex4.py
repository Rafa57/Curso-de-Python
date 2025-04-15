# Soma dos valores por chave em dicionários
entrada = [
    {'a': 1, 'b': 2},
    {'a': 3, 'c': 5},
    {'b': 1, 'c': 2}
]

def somar_chaves(lista):
    itens_somados = {}
    
    for dic in lista:
        for chave, valor in dic.items():
            if chave in itens_somados:
                itens_somados[chave] += valor
            else:
                itens_somados[chave] = valor        

    return itens_somados

print(somar_chaves(entrada))
# ----------------------------------------------------

# Remover caractere repetido mantendo a primeira ocorrência

def remove_dupli(text):
    clean_text = ''

    for char in text:
        clean_text += char if char not in clean_text else ''

    return clean_text

print(remove_dupli('abacate'))
print(remove_dupli('banana'))

# resolução
def remove_duplicata(text):
    seen = set()
    resultado = []

    for char in text:
        if char not in seen:
            seen.add(char)
            resultado.append(char)

    return ''.join(resultado)

# ---------------------------------------------------

# Agrupar palavras por tamanho

def group_by_len(words):
    word_dic = {}

    for word in words:
        word_dic[len(word)] = [n for n in words if len(n) == len(word)]
    
    return word_dic

print(group_by_len(["sol", "lua", "estrela", "céu", "mar", "universo"]))

# resolução
def palavras_agupadas(words):
    word_dic = {}

    for word in words:
        tamanho = len(word)

        if tamanho not in word_dic:
            word_dic[tamanho] = []

        word_dic[tamanho].append(word)

    return word_dic