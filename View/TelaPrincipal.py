import sys
from Utils.Helpers import Helpers
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from View.CadastrarUsuario import CadastrarUsuarioWindow
from View.CadastrarLivro import CadastrarLivroWindow

class TelaPrincipal(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.usuario = None
        ui_cadastrar_usuario = Helpers.get_base_path() + "/Ui/cadastrar_usuario.ui"
        ui_cadastrar_livro = Helpers.get_base_path() + "/Ui/cadastrar_livro.ui"

        self.cadastrar_usuario_window = CadastrarUsuarioWindow(ui_cadastrar_usuario)
        self.cadastrar_livro_window = CadastrarLivroWindow(ui_cadastrar_livro)

        self.btn_cadastrar_usuario.clicked.connect(self.abrir_tela_cadastro_usuario)
        self.btn_cadastrar_livro.clicked.connect(self.abrir_tela_cadastro_livro)

    def setar_usuario_logado(self, usuario: dict):
        self.usuario = usuario
        label = str(self.lbl_bem_vindo.text())
        self.lbl_bem_vindo.setText(label.replace('{usuario}', self.usuario.get('nome')))

    def abrir_tela_cadastro_usuario(self):
        self.cadastrar_usuario_window.show()

    def abrir_tela_cadastro_livro(self):
        self.cadastrar_livro_window.show()