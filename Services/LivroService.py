from Services.BaseService import BaseService
from Model.Livro import Livro
from Utils.Helpers import Helpers
from View.Alertas import Alertas

class LivroService(BaseService):
    def __init__(self) -> None:
        super().__init__()
        ui_alerta = Helpers.get_base_path() + "/Ui/alerta.ui"
        self.alerta_window = Alertas(ui_alerta)

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

        return self.bd.execute_query(livro, fetchOne=True)
    
    def listar_todos(self):
        return self.bd.execute_query(Livro.search_all())
    
    def procurar(self, valor):
        pesquisa = Livro.begin_search()
        pesquisa += Livro.or_search('titulo', valor, 'like', operador_logico=False)
        pesquisa += Livro.or_search('autor', valor, 'like')
        pesquisa += Livro.or_search('genero', valor, 'like')
        pesquisa += Livro.or_search('isbn', valor, 'like')

        return self.bd.execute_query(pesquisa)
    
    def emprestar_livro(self, codigo):
        livro = self.buscar_livro(codigo=codigo)

        if not livro or livro.get('status') != 'Disponível':
            self.alerta_window.set_mensagem('Livro não encontado ou não disponível!')
            self.alerta_window.set_color('red')
            self.alerta_window.show()
            return
        