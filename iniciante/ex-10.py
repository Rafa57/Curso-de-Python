import os
# os.system('cls') -> limpa o terminal

lista_de_compras = []

def inserir():
    while True:
        opcao = input('1.Adicionar\n2.Voltar\n\nEscolha uma opção: ')

        if opcao == '1':
            os.system('cls')

            adicionar = input('Adicione um item a lista: ')
            
            if adicionar.isalpha() == True:
                os.system('cls')
                lista_de_compras.append(adicionar)
                print(f'"{adicionar}" foi adicionado.')
            else:
                os.system('cls')
                print('Digite somente letras.')
            continue

        elif opcao == '2':
            os.system('cls')
            break

        else:
            os.system('cls')
            print('Opcao inválida')
            continue

def remover():
    while True:
        opcao = input('1.Remover\n2.Voltar\n\nEscolha uma opção: ')

        if opcao == '1':
            os.system('cls')
            indice = input('Digite a posição do item na lista: ')
            
            try:
                print(f'\nO item "{lista_de_compras[int(indice) - 1]}" foi removido da lista.\n')
                del lista_de_compras[int(indice) - 1]
            except ValueError:
                print('Digite apenas numeros inteiros\n')
            except IndexError:
                print('Não há itens nessa posição ou a lista está vazia.\n')
            except Exception:
                print('Erro desconhecido.')

        else:
            os.system('cls')
            break

def listar():
    while True:
        opcao = input('1.Ver lista\n2.Voltar\n\nEscolha uma opção: ')

        if opcao == '1':

            os.system('cls')
            if lista_de_compras != []:
                os.system('cls')
                print('-- Lista --')
                for ind, valor in enumerate(lista_de_compras, start=1):
                    print(ind, valor)
            else:
                os.system('cls')
                print('A lista está vazia.')
            print('\n')
            
        else:
            os.system('cls')
            break

def menu():
    
    while True:
        interface = input('----- MENU -----\n1.Adicionar item\n2.Remover item\n3.Ver lista\n0.Sair\n\nEscolha uma opção: ')

        if interface == '1':
            os.system('cls')
            inserir()
        elif interface == '2':
            os.system('cls')
            remover()           
        elif interface == '3':
            os.system('cls')
            listar()
        elif interface == '0':
            os.system('cls')
            print('Saiu')
            break
        else:
            os.system('cls')
            print('Digite apenas numeros válidos.\n')
            continue

menu()