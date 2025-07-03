# IMPORTS
# import sys
# print(sys.platform)

# from sys import platform  # CUIDADO: se uma variável for declarada com o mesmo nome, ela irá sobreescrever a importada
# print(platform)

# # alias 1 - import nome_modulo as apelido
# import sys as s
# print(s.platform)

# # alias 2 - from nome_modulo import objeto as apelido
# from math import sqrt as rq
# print(rq(25))

# # má prática - from nome_modulo import *
# from sys import *

#  MODULARIZAÇÃO
import aula23_m
import sys

print('Este modulo se chama', aula23_m.nome)
print('Este modulo se chama', __name__)

