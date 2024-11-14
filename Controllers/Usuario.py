from Config.Database import Database
from Model.Usuario import Usuario

class ControllerUsuario:
    def __init__(self) -> None:
        self.bd = Database()
    
ControllerUsuario.__name__ = "ControllerUsuario"