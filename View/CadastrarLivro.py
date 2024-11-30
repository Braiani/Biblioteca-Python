from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui
from Controllers.Livro import ControllerLivro

class CadastrarLivroWindow(QMainWindow):
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.actionCadastrarUsuario.triggered.connect(self.action)
    
    def action(self):
        print('clicou')
    
    def cancelar(self):
        self.close()

    def cadastrar(self):
        self.lbl_mensagem.setText('')
        titulo = self.input_titulo.text()
        autor = self.input_autor.text()
        genero = self.input_genero.text()
        codigo = self.input_codigo.text()

        livroController = ControllerLivro()

        if not titulo or not autor or not genero or not codigo:
            self.lbl_mensagem.setStyleSheet('color:red')
            self.lbl_mensagem.setText('Verifique todos os campos')
            
            return
        
        response = dict(livroController.cadastrarLivro(titulo, autor, genero, codigo))

        if not response.get('status'):
            self.lbl_mensagem.setStyleSheet('color:red')
            self.lbl_mensagem.setText(response.get('message'))
            return
        
        self.input_titulo.setText('')
        self.input_autor.setText('')
        self.input_genero.setText('')
        self.input_codigo.setText('')
        
        self.lbl_mensagem.setText('Livro salvo com sucesso!')
        self.lbl_mensagem.setStyleSheet('color:green')