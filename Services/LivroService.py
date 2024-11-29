from Services.BaseService import BaseService
from Model.Livro import Livro

class LivroService(BaseService):
    def __init__(self, titulo, autor, genero, codigo) -> None:
        super().__init__()
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo


    def cadastrar(self):
        livro = Livro(self.titulo, self.autor, self.genero, self.codigo)

        if self.buscar_livro(self.codigo):
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