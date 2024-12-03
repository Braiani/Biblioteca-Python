from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from Controllers.Livro import ControllerLivro

class ListarLivrosWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.livroController = ControllerLivro()
        
        self.atualizar_lista_livros()
        self.btn_procurar.clicked.connect(self.pesquisar_livro)
        self.lista_livros_widget.itemDoubleClicked.connect(self.emprestar_livro)

    def emprestar_livro(self):
        self.livroController.emprestarLivro(self.lista_livros_widget.currentItem().text().split(';')[0].split(': ')[1])
    
    def atualizar_lista_livros(self):
        self.livros = self.livroController.listarTodosLivros()

        livros_adicionar = []

        self.lista_livros_widget.clear()
        for livro in self.livros:
            livros_adicionar.append(f"Código: {livro.get('isbn')}; Título: {livro.get('titulo')}; Autor: {livro.get('autor')}; Gênero: {livro.get('genero')}; Status: {livro.get('status')}")
        
        self.lista_livros_widget.addItems(livros_adicionar)


    def pesquisar_livro(self):
        pesquisa = self.input_pesquisa.text()

        if pesquisa == '':
            self.atualizar_lista_livros()
            return
        
        self.lista_livros_widget.clear()
        livros_adicionar = []
        for livro in self.livroController.procurarLivro(pesquisa):
            livros_adicionar.append(f"Código: {livro.get('isbn')}; Título: {livro.get('titulo')}; Autor: {livro.get('autor')}; Gênero: {livro.get('genero')}; Status: {livro.get('status')}")

        self.lista_livros_widget.addItems(livros_adicionar)
    
    def show(self):
        self.lista_livros_widget.clear()
        self.atualizar_lista_livros()
        super().show()