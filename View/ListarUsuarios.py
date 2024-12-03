from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from Controllers.Usuario import ControllerUsuario

class ListarUsuariosWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)

        self.usuarioController = ControllerUsuario()

        self.atualizar_lista_usuarios()

    
    def atualizar_lista_usuarios(self):
        self.usuarios = self.usuarioController.listarTodosUsuarios()
        # for usuario in self.usuarios:
