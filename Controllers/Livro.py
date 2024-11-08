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

    def procurarLivro(self, coluna, valor, operador = "="):
        livro = self.bd.execute_query(Livro.search(coluna=coluna, valor=valor, operador=operador))

        print(livro)

    def atualizarLivro(self, coluna, novo_valor, where):
        self.bd.execute_query(Livro.update(coluna, novo_valor, where), commit=True)

    def deletarLivro(self, cod_livro):
        self.bd.execute_query(Livro.delete(cod_livro), commit=True)



# ControllerLivro().inserirLivro("Dom Casmurro", "Machado de Assis", "Suspense", 123)
ControllerLivro().procurarLivro('titulo', 'Casmurro', 'like')
# ControllerLivro().atualizarLivro('titulo', 'Dom Casmurro', 'Dom Casmurro')
# ControllerLivro().deletarLivro(123)