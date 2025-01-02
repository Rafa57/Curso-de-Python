nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade != '':
    print(f'Seu nome é "{nome}"\n')
    print(f'Seu nome invertido é "{nome[::-1]}"\n')

    if ' ' in nome:
        print(f'\nSeu nome contém espaços')
    else:
        print('Seu nome não contém espaços\n')
    
    print(f'Seu nome tem {len(nome)} caracteres\n')
    print(f'A primeira letra do seu nome é "{nome[0]}"\n')
    print(f'A última letra do seu nome é "{nome[-1]}"\n')
else:
    print('Desculpe, você deixou campos vazios.')