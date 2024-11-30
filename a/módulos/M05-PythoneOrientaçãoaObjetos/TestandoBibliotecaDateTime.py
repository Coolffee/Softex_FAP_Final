import datetime


class ItemBiblioteca:
    """Representa um item genérico da biblioteca (livro, revista, etc.)."""
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.emprestado = False  #Simples indicador de empréstimo

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print(f"Emprestando '{self.titulo}'...")
        else:
            raise Exception(f"O item '{self.titulo}' já está emprestado!")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print(f"Devolvendo '{self.titulo}'...")
        else:
            raise Exception(f"O item '{self.titulo}' não está emprestado!")


class Livro(ItemBiblioteca):
    """Representa um livro."""
    def __init__(self, titulo, autor, isbn, editora, ano):
        super().__init__(titulo, autor, isbn)
        self.editora = editora
        self.ano = ano

    def __str__(self):
        return f"{super().__str__()} \nEditora: {self.editora}, Ano: {self.ano}"


class Revista(ItemBiblioteca):
    """Representa uma revista."""
    def __init__(self, titulo, autor, isbn, edicao, data_publicacao):
        super().__init__(titulo, autor, isbn)
        self.edicao = edicao
        self.data_publicacao = data_publicacao

    def __str__(self):
        return f"{super().__str__()} \nEdição: {self.edicao}, Data: {self.data_publicacao.strftime('%d/%m/%Y')}"


class Membro:
    """Representa um membro da biblioteca."""
    def __init__(self, nome, id_membro):
        self.nome = nome
        self.id_membro = id_membro
        self.emprestimos = [] #Lista para controlar o que o membro pegou


class Biblioteca:
    """Sistema de gerenciamento da biblioteca."""
    def __init__(self):
        self.itens = []
        self.membros = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def emprestar_item(self, isbn, id_membro):
        """Empresta um item para um membro."""
        item = self._busca_item(isbn)
        membro = self._busca_membro(id_membro)
        if item and membro:
            item.emprestar()
            membro.emprestimos.append(item)
            print(f"{membro.nome} pegou '{item.titulo}'.")
        elif not item:
            print(f"Item com ISBN '{isbn}' não encontrado.")
        else:
            print(f"Membro com ID '{id_membro}' não encontrado.")

    def devolver_item(self, isbn, id_membro):
        """Devolve um item."""
        item = self._busca_item(isbn)
        membro = self._busca_membro(id_membro)
        if item and membro and item in membro.emprestimos:
            item.devolver()
            membro.emprestimos.remove(item)
            print(f"{membro.nome} devolveu '{item.titulo}'.")
        elif not item:
            print(f"Item com ISBN '{isbn}' não encontrado.")
        elif not membro:
            print(f"Membro com ID '{id_membro}' não encontrado.")
        else:
            print(f"O membro {membro.nome} não havia pegado este item.")

    def _busca_item(self, isbn):
        """Função auxiliar para buscar itens por ISBN."""
        for item in self.itens:
            if item.isbn == isbn:
                return item
        return None

    def _busca_membro(self, id_membro):
        """Função auxiliar para buscar membros por ID."""
        for membro in self.membros:
            if membro.id_membro == id_membro:
                return membro
        return None

#Exemplo básico de uso

#biblioteca = Biblioteca()
#biblioteca.adicionar_item(Livro("Dom Casmurro", "Machado de Assis", "978-85-01-07863-6", "Nova Fronteira", 1899))
#biblioteca.adicionar_item(Revista("Superinteressante", "Abril", "1234567890", 300, datetime.date(2024,4,1)))
#biblioteca.adicionar_membro(Membro("Maria", 1))
#biblioteca.emprestar_item("978-85-01-07863-6", 1)
#biblioteca.devolver_item("978-85-01-07863-6", 1)