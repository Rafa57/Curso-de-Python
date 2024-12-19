"""ISSO É UMA DocString"""
# sep = separador; end = insere algo no final
print(12, 32, sep=' - ', end='\n')
print(12, 32, sep=' - ', end=' algo') 

# escape
print("Rafael \"Santos\"")

#r
print(r"Rafael \"Santos\"")

# maneira correta
print('Rafael "Santos"')

#TIPOS DE DADOS

print("texto")#string

print(1234)#int

print(12.34)#float

print(True, False)#boolean

# função type
print(type('Bagre'))
print(type(123))
print(type(12.34))
print(type(True))

# CONVERSÃO DE TIPOS
print(1 + 2)
print('a' + 'b') #concatenação
print(int(2.5) + 5)
print(float(3) + 5)
print(str(3) + ' tres')
print(bool(' '))

# VARIÉVEIS
nome_completo = 'Rafael dos Santos Gomes'
soma_de_valores = 12 + 34
idade = 30
maior_de_idade = idade >= 18
print(f"nome: {nome_completo}", f"soma: {soma_de_valores}", f"Maior de idade?: {maior_de_idade}", sep=' | ')