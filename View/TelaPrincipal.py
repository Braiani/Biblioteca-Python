from Utils.Helpers import Helpers
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from View.CadastrarUsuario import CadastrarUsuarioWindow
from View.CadastrarLivro import CadastrarLivroWindow
from View.Alertas import Alertas
from View.ListarLivros import ListarLivrosWindow
from View.ListarUsuarios import ListarUsuariosWindow

class TelaPrincipal(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.usuario = None
        ui_cadastrar_usuario = Helpers.get_base_path() + "/Ui/cadastrar_usuario.ui"
        ui_cadastrar_livro = Helpers.get_base_path() + "/Ui/cadastrar_livro.ui"
        ui_listar_livros = Helpers.get_base_path() + "/Ui/listar_livros.ui"
        ui_listar_usuarios = Helpers.get_base_path() + "/Ui/listar_usuarios.ui"
        ui_alerta = Helpers.get_base_path() + "/Ui/alerta.ui"

        self.cadastrar_usuario_window = CadastrarUsuarioWindow(ui_cadastrar_usuario)
        self.cadastrar_livro_window = CadastrarLivroWindow(ui_cadastrar_livro)
        self.listar_livro_window = ListarLivrosWindow(ui_listar_livros)
        self.listar_livro_window = ListarLivrosWindow(ui_listar_livros)
        self.listar_usuarios_window = ListarUsuariosWindow(ui_listar_usuarios)
        self.alerta_window = Alertas(ui_alerta)

        self.btn_cadastrar_usuario.clicked.connect(self.abrir_tela_cadastro_usuario)
        self.btn_cadastrar_livro.clicked.connect(self.abrir_tela_cadastro_livro)
        self.btn_listar_livros.clicked.connect(self.abrir_tela_listar_livros)
        self.btn_listar_usuarios.clicked.connect(self.abrir_tela_listar_usuarios)

    def setar_usuario_logado(self, usuario: dict):
        self.usuario = usuario
        label = str(self.lbl_bem_vindo.text())
        self.lbl_bem_vindo.setText(label.replace('{usuario}', self.usuario.get('nome')))

    def abrir_tela_cadastro_usuario(self):
        if self.usuario.get('is_admin'):
            self.cadastrar_usuario_window.show()
        else:
            self.alerta_window.set_mensagem('Você não tem permissão para acessar essa funcionalidade!')
            self.alerta_window.set_color('red')
            self.alerta_window.show()

    def abrir_tela_cadastro_livro(self):
        self.cadastrar_livro_window.show()

    def abrir_tela_listar_livros(self):
        self.listar_livro_window.show()
        
    def abrir_tela_listar_usuarios(self):
        self.listar_usuarios_window.show()