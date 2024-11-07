import sys
sys.path[0] += '\\..'

from Config.Database import Database
from Model.Livro import Livro
class ControllerLivro:

    def __init__(self) -> None:
        self.bd = Database()
    
    def inserirLivro(self, titulo, autor, genero, cod_livro):
        livro = Livro(titulo, autor, genero, cod_livro)
        self.bd.execute_query(livro.create(), commit=True)

    def procurarLivro(self):
        livro = self.bd.execute_query(Livro.search('titulo', 'Casmurro', 'like'))

        print(livro)



# ControllerLivro().inserirLivro("Dom Casmurro", "Machado de Assis", "Suspense", 123)
ControllerLivro().procurarLivro()