from Model.Livro import Livro
from Services.LivroService import LivroService
class ControllerLivro:
    def __init__(self) -> None:
        self.livroService = LivroService()
    
    def cadastrarLivro(self, titulo, autor, genero, cod_livro):
        return self.livroService.cadastrar(titulo=titulo, autor=autor, genero=genero, codigo=cod_livro)

    def listarTodosLivros(self):
        return self.livroService.listar_todos()
        

    def procurarLivro(self, coluna, valor, operador = "="):
        livro = self.bd.execute_query(Livro.search(coluna=coluna, valor=valor, operador=operador))

        print(livro)

    def atualizarLivro(self, coluna, novo_valor, identificador, where):
        self.bd.execute_query(Livro.update(coluna, novo_valor, identificador, where), commit=True)

    def deletarLivro(self, coluna, cod_livro):
        self.bd.execute_query(Livro.delete(coluna, cod_livro), commit=True)

ControllerLivro.__name__ = "ControllerLivro"