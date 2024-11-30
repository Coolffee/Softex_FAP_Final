import sqlite3

#apenas uns testes basicos com db do sqlite

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

# Criar a tabela (se não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT
    )
''')

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cursor.execute("INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    print("Contato adicionado com sucesso!")

def listar_contatos():
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    if contatos:
        print("Contatos:")
        for contato in contatos:
            print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")
    else:
        print("Nenhum contato encontrado.")
# Se for continuar isso aqui lembrar de ajeitar o terminal pra 
# não ficar bugado e fazer testes unitarios no celular e etc
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")

conn.close()
