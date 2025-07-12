# Adiando a execução de funções

def sum_num(x, y):
    return x + y

def multi_num(x, y):
    return x * y

def execute(func, x):
    def wait(y):
        return func(x, y)
    return wait

sum_5 = execute(sum_num, 5)
multi_10 = execute(multi_num, 10)

print(sum_5(12))
print(multi_10(12))