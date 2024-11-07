import sys
sys.path[0] += '\\..'

from Config.Database import Database
from Model.Usuario import Usuario

class ControllerUsuario:
    def __init__(self) -> None:
        self.bd = Database()