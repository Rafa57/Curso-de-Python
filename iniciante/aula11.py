# imprecisão de ponto flutuante
import decimal

numero_1 = decimal.Decimal("0.1") # usado para calculos muito precisos
numero_2 = decimal.Decimal('0.7')
soma = numero_1 + numero_2
print(soma)
print(f'{soma:.2f}')

round()
print(round(soma, 2)) # ainda é um float

# split e join com list e str
frase = "   A lista    é    muito grande   "

frase_alterada = frase.split('é') # se não tiver argumento, a lista é dividida nos espaços

for i, frase in enumerate(frase_alterada):
    frase_alterada[i] = frase_alterada[i].strip() # corta os espaços das extremidades (lstrip() -> corta da esquerda / rstrip() -> corta da direita)

print('Depois do FOR: ', frase_alterada)

# melhor opção
frase_corrigida = []

for i, frase in enumerate(frase_alterada):
    frase_corrigida.append(frase_alterada[i].strip())

print(frase_alterada)
print(frase_corrigida)

# join
frase_unida = ' é '.join(frase_corrigida) # 'separador'.join(iterável)
print(frase_unida)

# lista de listas e seus indices
salas = [
    ['Maria', (10, 20, 30, 40, 50), 'Kaka', 'Rafael'],
    ['João','Brena', 'Roberto'],
    ['mateus', 'carla']
]

# print(salas[0][1][1])

for sala in salas:
    for i in sala:
       print(i)
       