# ENTRADA(input())

nome = input("What's your name? ")
print(f"Hi {nome}!")

numero_1 = input('Insert a number: ')
numero_2 = input('Insert another number: ')

int_num_1 = int(numero_1)
int_num_2 = int(numero_2)

print(f'A soma dos números é: {int_num_1 + int_num_2}')


# ESTRUTURAS CONDICIONAIS if - elif - else

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou no sistema.')

elif entrada == 'sair':
    print('Você saiu.')

else:
    print('Opção inválida. Digite apenas "entrar" ou "sair"')

condicao = True

if condicao:
    print('Este é o código do if')
else:
    print('falso')

print('Fora do if')


# OPERADORES DE COMPARAÇÃO

maior  = 2 > 1
maior_ou_igual = 2 >= 2
menor = 2 < 2
menor_ou_igual = 3 <= 2
igual = 2 == 2
diferente = 2 != 2

print("teste de texto")