from Model.Livro import Livro
from Services.LivroService import LivroService
class ControllerLivro:
    def __init__(self) -> None:
        self.livroService = LivroService()
    
    def cadastrarLivro(self, titulo, autor, genero, cod_livro):
        return self.livroService.cadastrar(titulo=titulo, autor=autor, genero=genero, codigo=cod_livro)

    def listarTodosLivros(self):
        return self.livroService.listar_todos()
        
    def procurarLivro(self, valor):
        return self.livroService.procurar(valor)
    
    def emprestarLivro(self, codigo):
        return self.livroService.emprestar_livro(codigo=codigo)

ControllerLivro.__name__ = "ControllerLivro"