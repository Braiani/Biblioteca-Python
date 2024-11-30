from Services.BaseService import BaseService
from Model.Livro import Livro

class LivroService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def cadastrar(self, titulo, autor, genero, codigo):
        livro = Livro(titulo, autor, genero, codigo)

        if self.buscar_livro(codigo):
            return {
                'status': False,
                'message': 'Livro já cadastrado'
            }

        if self.bd.execute_query(livro.create(), commit=True):
            return {
                'status': True,
                'message': 'Livro cadastrado com sucesso'
            }
    
    def buscar_livro(self, codigo):
        livro = Livro.search('isbn', codigo)

        return self.bd.execute_query(livro)
    
    def listar_todos(self):
        return self.bd.execute_query(Livro.search_all())