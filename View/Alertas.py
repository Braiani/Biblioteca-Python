from PyQt6.QtWidgets import QDialog
from PyQt6.uic import load_ui


class Alertas(QDialog):
    def __init__(self, ui_file, mensagem = '') -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)

        self.mensagem = mensagem

        self.btn_fechar.clicked.connect(self.close)
    
    def set_mensagem(self, mensagem):
        self.mensagem = mensagem

    def set_color(self, color):
        self.lbl_mensagem.setStyleSheet(f'color:{color}')

    def show(self):
        self.lbl_mensagem.setText(self.mensagem)
        super().show()