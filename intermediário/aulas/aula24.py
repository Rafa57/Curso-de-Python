# # introdução aos packages

# from sys import path
# import aula24_package.module
# from aula24_package.module import module_sum 
# from aula24_package import module
# from aula24_package.module import * # má prática

# print(*path, sep='\n')
# print(module_sum(12, 23))
# print(module.module_sum(12, 32))
# print(variable)
# -----------------------------------------
# from aula24_package.module import module_sum, say_anything

# print(__name__)
# print(module_sum(23, 45))
# say_anything()
# -------------------------------------------------------
from aula24_package import module_sum, variable
# print(aula24_package.double_x(5))

print(module_sum(23, 45))
print(variable)