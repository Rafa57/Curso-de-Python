# FUNÇÕES

def calculo(a, b): # PARÂMETROS -> VARIAVEIS passadas na DEFINIÇÃO da função
    c = (a + b) * (a**2 / b)
    print(f'Resultado: {c:.2f}')

calculo(11, 3) # ARGUMENTOS -> VALORES passados na CHAMADA da função

# ARGUMENTOS NOMEADOS E NÃO NOMEADOS

def operacao(x, y, z):
    print((z + x) * (z + y * x))

print(operacao) # refere-se ao endereço na memoria
print(operacao(6, 5, 4)) # argumento posicional -> a ordem importa
operacao(4, 5, 3)
operacao(5, y=4, z=7) # após um argumento nomeado ser definido, os seguintes argumentos também devem ser nomeados

# VALORES PADRÃO PARA PARÂMETROS

def soma(x, y, z=None):
    if z is not None:
        print(f'{x = } {y = } {z = } |  =', x + y + z)
    else:
        print(f'{x = } {y = }', x + y)
    

soma(444, 555, 0)
soma(444, 555)

# ESCOPO DE FUNÇÕES EM PYTHON

x = 10 # escopo global -> pode ser acessado em qualquer parte do algoritmo

def escopo():
    # global x -> Muda o escopo local de uma variável para global (não é uma boa prática)

    x = 23 # escopo local -> só pode ser acessado no bloco de código onde foi definido
    print(x)

    def outra_func():
        z = x + 12
        y = 6
        print(x, y, z)

    outra_func()

print(x)
escopo()
print(x)

 # RETORNO DAS FUNÇÕES (return)

def retornar(x, y):
    return x + y

z = 12
print(retornar(35, 67) * z // 10)

# ARGS -> argumentos não nomeados
# * - *args (empacotamento e desempacotamento)

x, y, *resto = 1, 2, 4, 5, 6, 7

# print(x, y, resto)

def somar(*args): # empacota todos os argumentos
    total = 0
    for numero in args:
        total += numero
    return total

resultado = 1,2,3,4
print(somar(*resultado))
outra_soma = sum(resultado)
print(outra_soma)


def lista(*args):
    print(args)
    return args

vari = 1, 2, 4, 5, 6, 7
lista(1,2,3)
soma = sum(lista(*vari))
print(soma)
# print(sum(somar(*resultado)))