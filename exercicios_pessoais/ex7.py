# somador de número pares
try:
    number_lst = []

    def input_lst():
        counter = 1

        while counter <= 10:
            number_lst.append(int(input(f"Digite o {counter}º número: ")))
            counter += 1

        return number_lst

    def sum_lst(lst):
        sum_num = 0
        for i in lst:
            if i % 2 == 0:
                sum_num += i
        
        return sum_num

    print(input_lst())
    print(sum_lst(number_lst))

except ValueError:
    print('Entrada inválida! Digite apenas número inteiros.')

# 
