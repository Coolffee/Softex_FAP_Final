import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="mydb"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descricao VARCHAR(255),
            data_criacao DATE,
            data_conclusao DATE,
            responsavel VARCHAR(100)
        )
    """)
    return conn, cursor

def inserir_tarefa(cursor, descricao, data_criacao, data_conclusao, responsavel):
    cursor.execute("""
        INSERT INTO tarefas (descricao, data_criacao, data_conclusao, responsavel)
        VALUES (%s, %s, %s, %s)
    """, (descricao, data_criacao, data_conclusao, responsavel))

def listar_tarefas(cursor):
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    if tarefas:
        for tarefa in tarefas:
            print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Data de Criação: {tarefa[2]}, Data de Conclusão: {tarefa[3]}, Responsável: {tarefa[4]}")
    else:
        print("Nenhuma tarefa encontrada.")

def editar_tarefa(cursor, id_tarefa, nova_descricao, nova_data_conclusao, novo_responsavel):
    cursor.execute("""
        UPDATE tarefas
        SET descricao = %s, data_conclusao = %s, responsavel = %s
        WHERE id = %s
    """, (nova_descricao, nova_data_conclusao, novo_responsavel, id_tarefa))

def excluir_tarefa(cursor, id_tarefa):
    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id_tarefa,))

def main():
    conn, cursor = connect_db()
    while True:
        print("1. Inserir Tarefa\n2. Listar Tarefas\n3. Editar Tarefa\n4. Excluir Tarefa\n5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Descrição: ")
            data_criacao = input("Data de Criação (YYYY-MM-DD): ")
            data_conclusao = input("Data de Conclusão (YYYY-MM-DD, pode ser nula): ")
            if not data_conclusao:
                data_conclusao = None
            responsavel = input("Responsável: ")
            inserir_tarefa(cursor, descricao, data_criacao, data_conclusao, responsavel)
            conn.commit()
        elif escolha == '2':
            listar_tarefas(cursor)
        elif escolha == '3':
            id_tarefa = input("ID da Tarefa: ")
            nova_descricao = input("Nova Descrição: ")
            nova_data_conclusao = input("Nova Data de Conclusão (YYYY-MM-DD, pode ser nula): ")
            if not nova_data_conclusao:
                nova_data_conclusao = None
            novo_responsavel = input("Novo Responsável: ")
            editar_tarefa(cursor, id_tarefa, nova_descricao, nova_data_conclusao, novo_responsavel)
            conn.commit()
        elif escolha == '4':
            id_tarefa = input("ID da Tarefa: ")
            excluir_tarefa(cursor, id_tarefa)
            conn.commit()
        elif escolha == '5':
            break
        else:
            print("Opção inválida, tente novamente.")

    conn.close()

if __name__ == "__main__":
    main()
