from Utils.Helpers import Helpers
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from Controllers.Usuario import ControllerUsuario
from View.TelaPrincipal import TelaPrincipal

class LoginWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.btn_logar.clicked.connect(self.logar)
        ui_principal = Helpers.get_base_path() + "/Ui/tela_principal.ui"

        self.main_window = TelaPrincipal(ui_file=ui_principal)

        self.show()
    
    def logar(self):
        self.label_msg.setText('')

        username = self.input_usuario.text()
        senha = self.input_senha.text()
        usuarioController = ControllerUsuario()

        if not username or not senha:
            self.exibir_erro('Campo de Usuário ou Senha está vazio!')
            return

        if usuarioController.logar(usuario=username, senha=senha):
            self.main_window.setar_usuario_logado(usuario=usuarioController.recupera_usuario_logado())
            self.main_window.show()
            self.close()

        self.exibir_erro()

    def exibir_erro(self, msg = 'Usuário e/ou Senha incorretos'):
        self.label_msg.setText(msg)