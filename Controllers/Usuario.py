from Config.Database import Database
from Services.LoginService import LoginService

class ControllerUsuario:
    def __init__(self) -> None:
        self.bd = Database()
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
        
    
ControllerUsuario.__name__ = "ControllerUsuario"