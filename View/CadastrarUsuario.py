from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.uic import load_ui

class CadastrarUsuarioWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
    
    def cadastrar(self):
        self.lbl_mensagem.setText('')
        nome = self.input_nome.text()
        cpf = self.input_cpf.text()
        telefone = self.input_telefone.text()
        senha = self.input_senha.text()
        confirmar_senha = self.input_confirmar_senha.text()
        if nome == "" or cpf == "" or telefone == "" or senha == "" or confirmar_senha == "":
            self.lbl_mensagem.setStyleSheet('color:red')
            self.lbl_mensagem.setText('Verifique todos os campos')
            
            return
        elif senha != confirmar_senha:
            self.lbl_mensagem.setStyleSheet('color:red')
            self.lbl_mensagem.setText('Os campos de Senha e confirmar senha devem ser iguais')
            
            return
        
        self.lbl_mensagem.setText('Usuário salvo com sucesso!')
        self.lbl_mensagem.setStyleSheet('color:green')