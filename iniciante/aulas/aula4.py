
# Operadores Lógicos (AND, OR, NOT)

opcao = input('''
    Escolha uma das opções abaixo:\n
      e = entrar\n
      s = sair
''')
senha = 1234
soli_senha = int(input('Digite a senha: '))

# AND
if opcao == "e":
    senha = input('Digite a senha: ')

    if opcao and soli_senha == senha:
        print('Voce entrou no sistema.\n')
    elif soli_senha != senha:
        print("\nSenha incorreta!\n")

else:
    print("\nVoce saiu do sistema.\n")

# OR
if (opcao == 'e' or opcao == 'E') and soli_senha == senha: #executa primeiro o que está entre parênteses
    print('Voce entrou no sistema.\n')
elif soli_senha != senha:
    print("\nSenha incorreta!\n")
else:
    print("\nVoce saiu do sistema.\n")

# NOT
senha = input('Digite a senha: ')

if not senha:
    print('Entrou no sistema')
else:
    print('Senha incorreta')


# AVALIAÇÃO DE CURTO CIRCUITO

# and
print(True and True and True)
print(True and 0 and True)

# or 
senha = input('senha:') or 'sem senha' # avaliação na variavel
print(senha)

print(True or False or False)
print(False or 0 or False or 'abc') # retorna o primeiro valor verdadeiro

# not
print(not True)
print(not False)

# OPERADORES IN E NOT IN

nome = 'Rafael'
print(nome[2])
print(nome[-3])

print('l' in nome)
print('fae' in nome)
print('j' in nome)
print('j' not in nome)
print('Raf' not in nome)

nome = input('digite seu nome: ')
encontrar = input('O que quer encontrar? ')

if encontrar in nome:
    print(f'"{encontrar}" está em {nome}')
else:
    print(f'"{encontrar}" não encontrado')