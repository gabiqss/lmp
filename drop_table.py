import sqlite3

def apagar_tabela(nome_do_banco, nome_da_tabela):
    # Conectando ao banco de dados
    conn = sqlite3.connect(nome_do_banco)
    cursor = conn.cursor()

    # Verificando se a tabela existe
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (nome_da_tabela,))
    tabela = cursor.fetchone()

    if tabela:
        # Removendo a tabela
        cursor.execute(f"DROP TABLE IF EXISTS {nome_da_tabela}")
        print(f"A tabela '{nome_da_tabela}' foi removida com sucesso.")
    else:
        print(f"A tabela '{nome_da_tabela}' não foi encontrada.")

    # Commitando as alterações e fechando a conexão
    conn.commit()
    conn.close()

# Chame a função passando o nome do seu banco de dados e o nome da tabela a ser removida
apagar_tabela("db.sqlite3", "django_content_type")
