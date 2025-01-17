# import math
import re
import sys

entrada = input('CPF: ')
# cpf = '187.864.760-17'.replace('.', '').replace('-','')

cpf = re.sub(
    r'[^0-9]', '', # substitui os caracteres que não forem numeros por ''
    entrada
    )

primeiro_char_repetido = entrada == entrada[0] * len(entrada)

if primeiro_char_repetido:
    print('caractere repetido')
    sys.exit()

# cpf_limpo = cpf.translate(str.maketrans('', '', '.-'))

nove_digitos = cpf[:9]

def multiplicar_cpf():
    lista_multi = []
    i = 0
    multi = 10
    while multi <= 10:
        try:
            calculo = int(nove_digitos[i]) * multi
            multi -= 1
            i += 1
            lista_multi.append(calculo)
        except IndexError:
            break

    return lista_multi

def somar_multi_cpf():
    resultado = 0
    for i in multiplicar_cpf():
        resultado += i

    return resultado

print(multiplicar_cpf())

multi_result = 10 * somar_multi_cpf()
resto = multi_result % 11
verificacao_digito = 0 if resto > 9 else resto
# print(f'O digito 1 é: {verificacao_digito}')

# resultado = sum(lista_multi)
# resultado = int(math.fsum(lista_multi))
# print(resultado)


# RESOLUÇÃO (PRIMEIRO DIGITO)-----------------------
nove_digitos = cpf[:9]

def multiplicar_cpf():
    multi = 10
    resultado = 0
    for digito in nove_digitos:
        resultado += int(digito) * multi
        multi -= 1
    
    return resultado

resto_1 = (multiplicar_cpf() * 10) % 11

verificacao_digito = resto if resto <= 9 else 0
print(f'O digito 1 é: {verificacao_digito}')
# -------------------------------------------------

# RESOLUÇÃO (SEGUNDO DIGITO)-----------------------
dez_digitos = cpf[:10]

def multiplicar_cpf():
    multi = 11
    resultado = 0
    for digito in dez_digitos:
        resultado += int(digito) * multi
        multi -= 1
    
    return resultado

resto_2 = (multiplicar_cpf() * 10) % 11

verificacao_digito = resto_2 if resto_2 <= 9 else 0
print(f'O digito 2 é: {verificacao_digito}')

cpf_calculado = f'{nove_digitos}{resto_1}{resto_2}'
print(cpf_calculado)
verificacao_cpf = 'CPF válido' if cpf == cpf_calculado else 'CPF inválido'
print(verificacao_cpf)
# --------------------------------------------------

