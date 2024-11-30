from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from Controllers.Livro import ControllerLivro
from Model.Livro import Livro

class ListarLivrosWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.livroController = ControllerLivro()
        
        self.atualizar_lista_livros()
    
    def atualizar_lista_livros(self):
        self.livros = self.livroController.listarTodosLivros()

        livros_adicionar = []

        for livro in self.livros:
            livros_adicionar.append(f"Código: {livro.get('isbn')}; Título: {livro.get('titulo')}; Autor: {livro.get('autor')}; Gênero: {livro.get('genero')}; Status: {livro.get('status')}")
        
        self.lista_livros_widget.addItems(livros_adicionar)
    
    def show(self):
        self.lista_livros_widget.clear()
        self.atualizar_lista_livros()
        super().show()