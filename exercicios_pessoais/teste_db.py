import sqlite3

# CONECTANDO AO BANCO DE DADOS
con = sqlite3.connect('data_base.db')
con.row_factory = sqlite3.Row
cursor = con.cursor()

# CRIANDO UMA ENTIDADE (TABELA)
con.execute("""
    CREATE TABLE IF NOT EXISTS doadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        valor FLOAT
    )
""")
con.commit()

# INSERINDO OS DADOS NO BANCO DE DADOS
def insert_doador():
    nome = input("Digite seu nome: ")
    idade = input('Digite a sua idade: ')
    valor = input("Digite o valor: ").replace(',', '.')

    cursor.execute("INSERT INTO doadores (nome, idade, valor) VALUES (?, ?, ?)", (nome, idade, valor))
    con.commit()

# CONSULTANDO DADOS
def show_table():
    cursor.execute('SELECT * FROM doadores')
    doadores = cursor.fetchall()

    if doadores:
        for doador in doadores:
            print(tuple(doador))
    else:
        print("A tabela está vazia")

# ATUALIZANDO DADOS
def update_doador():
    doador_id = int(input("Digite o ID: "))

    cursor.execute('SELECT * FROM doadores WHERE id = ?', (doador_id,))
    doador = cursor.fetchone()

    if doador:
        atualizar_dado = input("O que quer atualizar?: ")

        if atualizar_dado == 'idade':
            nova_idade = input("Digite a nova idade: ")
            cursor.execute("UPDATE doadores SET idade = ? WHERE id = ?", (nova_idade, doador_id))
            
        elif atualizar_dado == 'nome':
            novo_nome = input("Digite o novo nome: ")
            cursor.execute("UPDATE doadores SET nome = ? WHERE id = ?", (novo_nome, doador_id))
            
        elif atualizar_dado == 'valor':
            novo_valor = input("Digite o novo valor: ")
            cursor.execute("UPDATE doadores SET valor = ? WHERE id = ?", (novo_valor, doador_id))
        
        else:
            print('Campo inválido!')
        
        con.commit()

    else:
        print("ID não encontrado!")

# # DELETANDO DADOS
def del_doador():
    id_doador = int(input("Digite o ID: "))

    cursor.execute("SELECT * FROM doadores WHERE id = ?", (id_doador,))
    doador_deletado = cursor.fetchone()

    if doador_deletado:
        cursor.execute("DELETE FROM doadores WHERE id = ?", (id_doador,))
        con.commit()

        print(f"O doador {doador_deletado['nome']} foi deletado.")
    else:
        print("ID não encontrado")

# RESET DO BANCO DE DADOS
def reset_tabela():
    confirmacao = input("Quer resetar a tabela? [S] ou [N]: ")

    if confirmacao.lower() == 's':
        confirmacao2 = input('Tem certeza? [S] ou [N]: ')

        if confirmacao2.lower() == 's':
            cursor.execute("DELETE FROM doadores")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='doadores'")
            con.commit()

            cursor.execute('SELECT * FROM doadores')
            doadores = cursor.fetchall()

            if not doadores:
                print(f"A tabela 'doadores' foi resetada.")

        else:
            print('Reset de tabela cancelado!')
        
    elif confirmacao.lower() == 'n':
        print("Reset de tabela cancelado!")
    else:
        print("Digite somente uma das opções: [S] ou [N]")

# MENU
show_table()

# insert_doador()

# show_table()

# update_doador()

# del_doador()

# reset_tabela()

con.close()