# tipos imutáveis: str, int, float, bool

# string = 'rafael santos'
# variavel = f'{string[:7]}BOB{string[8:]}'
# # string[7] = 'Bob' # gera um erro
# print(variavel)
# print(variavel[7])
# print(string.zfill(25))

# LAÇOS DE REPETIÇÃO (loop)

# WHILE
# operadores de atribuição
# +=  -=  *=  /=  //=  **=  %=

# contador = 0
# while contador <= 5:

#     contador += 1

#     if contador == 4:
#         print('o quatro sumiu')
#         continue

#     print(contador)

# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1

# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
#     linha += 1

# calculadora
print('--ESCOLHA UMA OPÇÃO--')
print('1. Calcular\n2. Sair')
opcao = input()

if opcao == '1':
    
    while True:

        num1 = input('Digite o primeiro número: ')
        operador = input('''Escolha a operação (+  -  *  /): ''')
        num2 = input('Digite o segundo número: ')

        num1 = int(num1)
        num2 = int(num2)

        if operador == '+':
            print(num1 + num2)
        elif operador == '-':
            print(num1 - num2)
        elif operador == '*':
            print(num1 * num2)
        elif operador == '/':
            print(num1 / num2)

        sair = input('Quer sair? [s]: ').lower().startswith('s')
        if sair is True:
            print('Saiu')
            break
else:
    print('Saiu')
