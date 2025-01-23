
def verificar_inteiro(numero):

    try:
        numero = int(numero)
        return numero

    except ValueError:
        print('O número digitado não é inteiro.')
        return None

def verificar_impar_par(valor):
    
    valor = int(valor)
    if valor % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar!')

def verificar_hora_valida(hora):
    
    try:
        hora = int(hora)
        return hora

    except ValueError:
        print('Digite somente números inteiros')
        return None
    
def verificar_hora(hora):

    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida.')

def verificar_nome(nome):

    if not nome.isalpha():
        print('Digite apenas letras')
        return None

    tamanho = len(nome)

    if tamanho > 1:
        if tamanho <= 4:
            print('Seu nome é curto')
        elif tamanho > 4 and tamanho <= 6:
            print('Seu nome é normal')
        elif tamanho > 6:
            print("Seu nome é muito grande.")
    else:
        print('Digite mais de uma letra.')

# IMPAR OU PAR
numero_digitado = input('Digite um número inteiro: ')
numero = verificar_inteiro(numero_digitado)

if numero is not None:
    verificar_impar_par(numero)

# HORA
horario = input('Que horas são? ')
hora = verificar_hora_valida(horario)

if hora is not None:
    verificar_hora(hora)

# NOME
nome_do_usuario = input('Digite o seu nome: ')

if nome_do_usuario is not None: 
    verificar_nome(nome_do_usuario)