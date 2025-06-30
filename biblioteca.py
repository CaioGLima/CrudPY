from livro import Livro
import banco

#Cria uma lista para armazenar os livros
class Biblioteca:
    def __init__(self):
        banco.criar_tabela()  # Garante que a tabela exista

#Adiciona um novo livro a listá
    def adicionar_livros( self, livro: Livro):
        banco.inserir_livro(livro)
        print("\n Livro adicionado com sucesso!")
        print(f"{livro}")

#Mostra os livros cadastrados
    def listar_livros(self):
        livros = banco.buscar_livros()

        if not livros:
            print("Nenhum livro cadastrado")
            return
        
        conn = banco.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM livros")
        ids = [linha[0] for linha in cursor.fetchall()]
        conn.close()
        
        print("\n--- Lista de Livros ---")
        for idx, livro in enumerate(livros, 1):
            print(f"{idx}. {livro}")

#Atualiza informações de um livro existente
    def editar_livro(self, id_livro, novo_livro: Livro):
        banco.atualizar_livro(id_livro, novo_livro)
        print("\n Livro atualizado com sucesso!")

#Deleta o livro existente
    def remover_livro(self, id_livro):
        banco.remover_livro(id_livro)
        print("\n Livro removido com sucesso!")