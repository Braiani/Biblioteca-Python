from Model.Usuario import Usuario
from Config.Database import Database

class LoginService:
    def __init__(self, usuario, senha) -> None:
        self.usuario = usuario
        self.senha = senha
        self.bd = Database()


    def verificar_login(self):
        userModel = Usuario.begin_search()
        userModel += Usuario.and_search('usuario',self.usuario, '=', operador_logico=False)
        userModel += Usuario.and_search('senha',self.senha, '=')
        
        usuarios = self.bd.execute_query(userModel)
        
        if not usuarios:
            return False
        
        return usuarios
        

LoginService.__name__ = "LoginService"