from Services.LoginService import LoginService
from Services.UsuarioService import UsuarioService

class ControllerUsuario:
    def __init__(self) -> None:
        self.usuario_logado = None
    
    def logar(self, usuario, senha):
        loginService = LoginService(usuario=usuario, senha=senha)

        usuario = loginService.verificar_login()
        if not usuario:
            return False
        
        self.usuario_logado = usuario

        return True
    
    def recupera_usuario_logado(self):
        if self.usuario_logado == None:
            return False
        
        return self.usuario_logado
    
    def cadastrar(self, nome, usuario, cpf, telefone, senha):
        usuarioService = UsuarioService(nome=nome, usuario=usuario, cpf=cpf, telefone=telefone, senha=senha)
        return usuarioService.cadastrar()

        
    
ControllerUsuario.__name__ = "ControllerUsuario"