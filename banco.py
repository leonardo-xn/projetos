import sqlite3

def conectar():

    return sqlite3.connect("usuarios.db")


def criar_tabela():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        senha TEXT
    )
    """)

    conexao.commit()
    conexao.close()


def cadastrar(usuario, senha):

    conexao = conectar()

    cursor = conexao.cursor()

    try:

        cursor.execute("""
        INSERT INTO usuarios (usuario, senha)
        VALUES (?, ?)
        """, (usuario, senha))

        conexao.commit()

        return True

    except:

        return False

    finally:

        conexao.close()


def login(usuario, senha):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario=? AND senha=?
    """, (usuario, senha))

    usuario_encontrado = cursor.fetchone()

    conexao.close()

    return usuario_encontrado


criar_tabela()