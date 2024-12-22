nome = 'Rafael Santos'
altura = 1.75
peso = 78
imc = ... # ellipsis = é um placeholder esperando o algoritmo a ser escrito. (Não gera erros no código)
imc = peso / (altura * altura)

# f-strings
print(f"{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}.")

# format()
a = "O "
b = "número é "
c = 125

string = 'a = {0} b = {1} c = {2:.2f}'
formato = string.format(a, b, c) #usando métodos de uma objeto
print(formato)

# paramentro nomeado
string = 'a = {nome1} b = {nome2} c = {nome3:.2f}'
parametro_nomeado = string.format(nome1= a, nome2= b, nome3= c) # tudo que vier depois de um parametro nomeado também precisa se nomeado

print(parametro_nomeado)