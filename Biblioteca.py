from Model.Livro import Livro
from Model.Usuario import Usuario

class Biblioteca:
    acervo = []

    @staticmethod
    def emprestar(livro: Livro, usuario: Usuario):
        livro.emprestar_livro(usuario)
        usuario.emprestar(livro)