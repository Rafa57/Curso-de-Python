# soma dos elementos de uma lista
def sum_list_1(lst):
    return sum(lst)

def sum_list_2(lst):
    sum_lst = 0
    for i in lst:
        sum_lst += i
    return sum_lst
print(sum_list_1([14, 2, 23, 34, 45, 67, 12]))
print(sum_list_2([14, 2, 23, 34, 45, 67, 12]))

#numeros pares até n
def pair_num(num):
    return [n for n in range(num + 1) if n % 2 == 0]
print(pair_num(12))

#contar palavras em uma frase
def word_counter(s):
    return len(s.split())
print(word_counter("Hoje o céu está lindo"))

# dicionário de contagem de palavras
def w_count(s):
    s = s.split()
    dictio = {}
    for word in s:
       dictio[word] = dictio.get(word, 0) + 1
    return dictio
print(w_count("olá mundo olá universo"))

# Verificar se todos os elementos são do mesmo tipo
def type_verify(lst):
    if not lst:
        return 'lista vazia'
    for i in lst:
        if type(i) != type(lst[0]):
            return False
    return True
print(type_verify([1, 2, 3, 4]))
print(type_verify(['a', 1, 'd']))

# verificador de cpf simples
def cpf_verify(cpf):
    cpf = cpf.strip()
    return len(cpf) == 11 and cpf.isdigit()

print(cpf_verify("12345678900"))   # True
print(cpf_verify("1234a789000"))  # False  
print(cpf_verify("12345678"))    # False