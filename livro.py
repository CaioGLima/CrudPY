class Livro:
    def __init__(self, titulo, autor, ano, genero, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.disponivel = disponivel 

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        return f"{self.titulo} ({self.ano}) - {self.autor} | {self.genero} [{status}]"
    
        