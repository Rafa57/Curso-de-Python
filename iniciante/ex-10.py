lista_de_compras = []

def inserir():
    while True:
        opcao = input('1.Adicionar\n2.Voltar\n\nEscolha uma opção: ')

        if opcao == '1':
            adicionar = input('Adicione um item a lista: ')
            
            if adicionar.isalpha() == True:
                lista_de_compras.append(adicionar)
            else:
                print('Digite somente letras.')
            continue

        elif opcao == '2':
            break

        else:
            print('Opcao inválida')
            continue

    
def remover():
    while True:
        opcao = input('1.Remove\n2.Voltar\n\nEscolha uma opção: ')

        if opcao == '1':
            indice = input('Digite a posição do item na lista: ')
            print(f'\nO item "{lista_de_compras[int(indice) - 1]}" foi removido da lista.\n')
            del lista_de_compras[int(indice) - 1]

            continue

        else:
            break

def listar():
    while True:
        opcao = input('1.Ver lista\n2.Voltar\n\nEscolha uma opção: ')

        if opcao == '1':
            if lista_de_compras != []:
                print('-- Lista --')

                for a, b in enumerate(lista_de_compras, start=1):
                    print(a, b)

            else:
                    print('A lista está vazia.')
            print('\n')
        else:
            break

def menu():
    
    while True:
        interface = input('\n----- MENU -----\n1.Adicionar item\n2.Remover item\n3.Ver lista\n0.Sair\n\nEscolha uma opção: ')

        if interface == '1':
            inserir()
            continue
        if interface == '2':
            remover()
            continue
        if interface == '3':
            listar()
            continue
        if interface == '0':
            print('Saiu')
            break
        else:
            print('Digite apenas numeros válidos.')
            continue

menu()