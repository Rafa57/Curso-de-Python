# Try, except, else e finally

try:
    lista1 = [n for n in range(12)]
    p = [n for n in range(23)]
    
    print('linha 1')
    print(p['a']) # TypeError
    print(lista1[15]) # IndexError
    print(lista2[6]) # NameError
    print('linha 2')
    
except TypeError as e:
    print('Error: ', e)

except (IndexError, NameError) as error:
    print('Msg: ', error)
    print('Nome: ', error.__class__.__name__)

except Exception:
    # TRATA QUALQUER TIPO DE ERRO, POIS É A SUPERCLASSE DE TODAS A EXCEÇÕES
    print('Erro desconhecido')

# -------------------------------------------------------------------

print('Erro silenciado')

# TRY, EXCEPT, ELSE E FINALLY
try:
    a = 1
    print(a[1])
except TypeError:
    print("Erro: type")

else:  # executa somente se não houver erros (mas é redundante, pois o try faz o mesmo)
    print("Não houve erro")

finally: # finally sempre é executado, independente de erro ou não
    print(2)

# -----------------------------------------------------------------


#  RAISE - LANÇANDO EXCEÇÕES (ERROS)
print(123)
# raise ValueError("deu erro")
print(456)

def erro_div_0(n):
    if n == 0:
        raise ZeroDivisionError("Não é possível dividir por 0")
    return True

def tp_erro(n):
    if not isinstance(n, (float, int)):
        raise TypeError("Só é permitido a divisão por números inteiros ou decimais")
    return True

def dividir(a, b):
    erro_div_0(b)
    tp_erro(a)
    tp_erro(b)

    return a/b

def index(i):
    try:
        a = []
        return a[i]
    except IndexError:
        print('erro')
        raise  # RAISE lança um erro definido 
                # dentro de um except, ele relança o erro do except, o que é redundante, já que o try já lança esse erro
                # É usado em um except quando se quer fazer algo dentro dele

print(dividir(12, '0'))
print(index(2))