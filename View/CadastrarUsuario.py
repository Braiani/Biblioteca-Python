from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from Controllers.Usuario import ControllerUsuario

class CadastrarUsuarioWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        self.btn_cancelar.clicked.connect(self.close)
    
    def cadastrar(self):
        self.lbl_mensagem.setText('')
        nome = self.input_nome.text()
        usuario = self.input_usuario.text()
        cpf = self.input_cpf.text()
        telefone = self.input_telefone.text()
        senha = self.input_senha.text()
        confirmar_senha = self.input_confirmar_senha.text()

        usuarioController = ControllerUsuario()

        if not nome or not cpf or not telefone or not senha or not confirmar_senha:
            self.lbl_mensagem.setStyleSheet('color:red')
            self.lbl_mensagem.setText('Verifique todos os campos')    
            return
        
        elif senha != confirmar_senha:
            self.lbl_mensagem.setStyleSheet('color:red')
            self.lbl_mensagem.setText('Os campos de Senha e confirmar senha devem ser iguais')
            return
        
        cadastrar_usuario = usuarioController.cadastrar(nome=nome, usuario=usuario, cpf=cpf, telefone=telefone, senha=senha)
        if cadastrar_usuario:
            if cadastrar_usuario.get('status'):
                color = 'green'
            else:
                color = 'red'

            self.lbl_mensagem.setStyleSheet(f'color:{color}')
            self.lbl_mensagem.setText(cadastrar_usuario.get('mensagem'))

            if cadastrar_usuario.get('status'):
                self.input_nome.setText('')
                self.input_usuario.setText('')
                self.input_cpf.setText('')
                self.input_telefone.setText('')
                self.input_senha.setText('')
                self.input_confirmar_senha.setText('')

            return

        self.lbl_mensagem.setStyleSheet('color:red')
        self.lbl_mensagem.setText('Erro ao salvar usuário')