def verify(function):
    result = [num for num in function if (num ** (1 / 2)) % 2 == 0]
    return result

def pair_num(len):
    create_lst = [item for item in range(1, len + 1)]
    return create_lst

print(verify(pair_num(1000)))