from Model.Usuario import Usuario
from Services.BaseService import BaseService

class UsuarioService(BaseService):
    def __init__(self, nome, cpf, telefone, senha) -> None:
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
    
    def cadastrar(self):
        userModel = Usuario(self.nome, self.cpf, self.telefone, self.senha)
        
        if self.buscar_usuario():
            return {
                'mensagem': 'Usuario ja cadastrado',
                'status': False
            }

        userModel = Usuario.create()

        result = self.bd.execute_query(userModel, commit=True)
        if not result:
            return {
                'mensagem': 'Erro ao salvar usuario',
                'status': False
            }
                
        return {
            'mensagem': 'Usuario salvo com sucesso!',
            'status': True
        }
    
    def buscar_usuario(self):
        userModel = Usuario.begin_search()
        userModel += Usuario.and_search('cpf', self.cpf, '=')
        
        return self.bd.execute_query