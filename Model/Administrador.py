from Model.Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome: str, email: str, senha: str) -> None:
        super().__init__(nome, email, senha)
        
    
    