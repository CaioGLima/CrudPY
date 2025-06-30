from livro import Livro
from biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:
    print("\n=== MENU ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Atualizar livro")
    print("4. Remover livro")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input ("Ano: "))
        genero = input ("Gênero: ")

        livro = Livro(titulo, autor, ano, genero)
        biblioteca.adicionar_livros(livro)

    elif opcao == "2":
        biblioteca.listar_livros()

    elif opcao == "3":
        biblioteca.listar_livros()
        try:
            id_livro = int(input("\nDigite o ID do livro que deseja editar: "))
            print("Digite os novos dados do livro: ")
            titulo = input("Novo título> ")
            autor = input("Novo autor: ")
            ano = int(input("Novo ano: "))
            genero = input("Novo genero: ")

            novo_livro = Livro(titulo, autor, ano,genero)
            biblioteca.editar_livro(id_livro, novo_livro)

        except ValueError:
            print(" Entrada inválida. O ID e o ano devem ser números.")

    elif opcao == "4":
        biblioteca.listar_livros()
        try:
            id_livro = int(input("\nDigite o ID do livro que deseja remover: "))
            confirmacao = input("Tem certeza que deseja remover este livro? (s/n): ").lower()
            if confirmacao == "s":
                biblioteca.remover_livro(id_livro)
            else:
                print(" Remoção cancelada.")
        except ValueError:
            print(" Entrada inválida. O ID deve ser um número.")

    elif opcao == "5":
        print("Programa Encerrado")
        break

else:
        print("Opção Não é Válida, Porfavor selecione uma das opções existentes")