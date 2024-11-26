import sys
from Utils.Helpers import Helpers
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.uic import load_ui
from View.CadastrarLivro import CadastrarLivroWindow
from View.CadastrarUsuario import CadastrarUsuarioWindow

class LoginWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.btn_logar.clicked.connect(self.action)
    
    def action(self):
        print('clicou')

    def logar(self):
        pass

ui_cadastrar_livro = Helpers.get_base_path() + "/Ui/cadastrar_livro.ui"
ui_cadastrar_usuario = Helpers.get_base_path() + "/Ui/cadastrar_usuario.ui"