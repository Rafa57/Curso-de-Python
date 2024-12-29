
# Operadores Lógicos (AND, OR, NOT)

opcao = input('''
    Escolha uma das opções abaixo:\n
      e = entrar\n
      s = sair
''')
senha = 1234
soli_senha = int(input('Digite a senha: '))

# # AND
# if opcao == "e":
#     senha = input('Digite a senha: ')

#     if opcao and soli_senha == senha:
#         print('Voce entrou no sistema.\n')
#     elif soli_senha != senha:
#         print("\nSenha incorreta!\n")

# else:
#     print("\nVoce saiu do sistema.\n")

# OR
if (opcao == 'e' or opcao == 'E') and soli_senha == senha: #executa primeiro o que está entre parênteses
    print('Voce entrou no sistema.\n')
elif soli_senha != senha:
    print("\nSenha incorreta!\n")
else:
    print("\nVoce saiu do sistema.\n")

# AVALIAÇÃO DE CURTO CIRCUITO

# and
print(True and True and True)
print(True and 0 and True)

# or 
senha = input('senha:') or 'sem senha' # avaliação na variavel
print(senha)

print(True or False or False)
print(False or 0 or False or 'abc') # retorna o primeiro valor verdadeiro