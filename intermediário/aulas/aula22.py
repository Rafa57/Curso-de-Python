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
    

print('Erro silenciado')