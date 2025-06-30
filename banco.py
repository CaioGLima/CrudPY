import sqlite3

from livro import Livro

#Conecta ao banco
def conectar():
    return sqlite3.connect("Biblioteca.db")

#Cria a tabela se não existir
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL,
            genero TEXT NOT NULL,
            disponivel INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def inserir_livro(livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, genero, disponivel)
       VALUES (?, ?, ?, ?, ?)
    """, (livro.titulo, livro.autor, livro.ano, livro.genero, int(livro.disponivel)))
    conn.commit()
    conn.close() 

def buscar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, autor, ano, genero, disponivel FROM livros")
    linhas = cursor.fetchall()
    conn.close()

    livros = []
    for linha in linhas:
        titulo, autor, ano, genero, disponivel = linha
        livro = Livro(titulo, autor, ano, genero, bool(disponivel))
        livros.append(livro)

    return livros

def atualizar_livro(id_livro, novo_livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE livros
        SET titulo = ?, autor = ?, ano = ?, genero = ?, disponivel = ?
        WHERE id = ?
    """, (novo_livro.titulo, novo_livro.autor, novo_livro.ano, novo_livro.genero, int(novo_livro.disponivel), id_livro))
    conn.commit()
    conn.close()

def remover_livro(id_livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    conn.commit()
    conn.close()

