import sys
from Model.Usuario import Usuario
from Model.Livro import Livro
from Biblioteca import Biblioteca
from Controllers.Livro import ControllerLivro
from Utils.Helpers import Helpers
from PyQt6.uic import load_ui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow


class MainWindows(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)


if __name__ == "__main__":
    ui_file = Helpers.get_base_path() + "/Ui/cadastrar_livro.ui"

    app = QApplication(sys.argv)
    window = MainWindows(ui_file)
    window.show()
    sys.exit(app.exec())