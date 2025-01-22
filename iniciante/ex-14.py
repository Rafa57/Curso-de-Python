# CRIE FUNÇÕES QUE DUPLICAM, TRIPLICAM E QUADRIPLICAM O NUMERO RECEBIDO COMO PARAMETRO

def create_multi(multi):
    def result(number):
        return multi * number
    
    return result

multi_2 = create_multi(2)
multi_3 = create_multi(3)
multi_4 = create_multi(4)

print(multi_2(6))
print(multi_3(6))
print(multi_4(6))