from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.uic import load_ui

class CadastrarLivroWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        self.actionCadastrarUsuario.triggered.connect(self.action)
    
    def action(self):
        print('clicou')

    def cadastrar(self):
        self.lbl_mensagem.setText('')
        titulo = self.input_titulo.text()
        autor = self.input_autor.text()
        genero = self.input_genero.text()
        codigo = self.input_codigo.text()
        if titulo == "" or autor == "" or genero == "" or codigo == "":
            self.lbl_mensagem.setStyleSheet('color:red')
            self.lbl_mensagem.setText('Verifique todos os campos')
            
            return
        self.lbl_mensagem.setText('Livro salvo com sucesso!')
        self.lbl_mensagem.setStyleSheet('color:green')