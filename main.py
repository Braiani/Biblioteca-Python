import sys
from Model.Usuario import Usuario
from Model.Livro import Livro
from Biblioteca import Biblioteca
from Controllers.Livro import ControllerLivro
from Utils.Helpers import Helpers
from PyQt6.QtWidgets import QApplication
from View.CadastrarLivro import CadastrarLivroWindow
from View.CadastrarUsuario import CadastrarUsuarioWindow


if __name__ == "__main__":
    ui_cadastrar_livro = Helpers.get_base_path() + "/Ui/cadastrar_livro.ui"
    ui_cadastrar_usuario = Helpers.get_base_path() + "/Ui/cadastrar_usuario.ui"

    app = QApplication(sys.argv)
    window = CadastrarLivroWindow(ui_cadastrar_livro)
    # window = CadastrarUsuarioWindow(ui_cadastrar_usuario)
    window.show()
    sys.exit(app.exec())