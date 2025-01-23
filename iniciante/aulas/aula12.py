# # desempacotamento em chamadas de funções e métodos

nome = 'RAFAEL'
lista = ['ra', 'fa', 'el', 1, 2, 3]
tupla = ('la', 'li', 'nha')
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a, b, *_, c, g = lista
print(a, c)


# triangulo de asteriscos centralizado
# string = ''

# while len(string) <= 26:
#     string += 2 * '*'
#     print(f'{string:^28}') # centraliza a string inserindo espaços(ou um separador antes do '^' {string:-^28})

for nome in lista:
    print(nome, end=' ')

print('ra', 'fa', 'el', 1, 2, 3)
print(*lista) # faz a mesma coisa que o print acima / *variável -> passa todos os itens como argumentos no print

print(*array, sep='\n')

# OPERADOR TERNÁRIO

cor = 'Vermelho'
carro = 'compro' if cor == 'Vermelho' else 'não compro'

print(carro)

digito = 10
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('valor' if True else 'outro' if True else 'Fim')