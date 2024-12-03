from Model.Usuario import Usuario
from Services.BaseService import BaseService

class LoginService(BaseService):
    def __init__(self, usuario, senha) -> None:
        super().__init__()
        self.usuario = usuario
        self.senha = senha


    def verificar_login(self):
        userModel = Usuario.begin_search()
        userModel += Usuario.and_search('usuario',self.usuario, '=', operador_logico=False)
        userModel += Usuario.and_search('senha',self.senha, '=')
        
        usuarios = self.bd.execute_query(userModel, fetchOne=True)
        
        if not usuarios:
            return False
        
        return usuarios
        

LoginService.__name__ = "LoginService"