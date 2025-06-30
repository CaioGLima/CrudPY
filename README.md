# CrudPY
Projeto para estudos, um CRUD - Create, Read, Update, Delete.

# Sistema de Cadastro de Livros (CRUD com Python e SQLite)

## Sobre o Projeto

Este é um projeto de estudo desenvolvido em Python, que permite gerenciar uma biblioteca de livros pessoais diretamente pelo terminal. A aplicação implementa as funcionalidades básicas de um CRUD — Criar, Ler, Atualizar e Deletar livros — utilizando Programação Orientada a Objetos (POO) e banco de dados SQLite.

##  Tecnologias Utilizadas

- Python 3
- SQLite3
- Programação Orientada a Objetos (POO)

## Funcionalidades

-  Adicionar um novo livro (título, autor, ano e gênero)
-  Listar todos os livros cadastrados
-  Atualizar os dados de um livro já cadastrado
-  Remover um livro da biblioteca
-  Interface de menu interativo no terminal

## Estrutura de Arquivos
├── main.py # Arquivo principal com o menu
├── livro.py # Classe Livro
├── biblioteca.py # Classe Biblioteca com métodos de controle
├── banco.py # Conexão e operações com SQLite
├── biblioteca.db # Banco de dados SQLite gerado automaticamente
