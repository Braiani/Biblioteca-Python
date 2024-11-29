from Model.Usuario import Usuario
from Services.BaseService import BaseService

class UsuarioService(BaseService):
    def __init__(self, nome, usuario, cpf, telefone, senha) -> None:
        super().__init__()
        self.nome = nome
        self.usuario = usuario
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
    
    def cadastrar(self):
        userModel = Usuario(nome=self.nome, usuario=self.usuario, cpf=self.cpf, telefone=self.telefone, senha=self.senha)
        
        if self.buscar_usuario():
            return {
                'mensagem': 'Usuario ja cadastrado',
                'status': False
            }

        userModel = userModel.create()

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
        userModel += Usuario.and_search('cpf', self.cpf, '=', operador_logico=False)
        
        return self.bd.execute_query(userModel)