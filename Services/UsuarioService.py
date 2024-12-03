from Model.Usuario import Usuario
from Services.BaseService import BaseService

class UsuarioService(BaseService):
    def __init__(self) -> None:
        super().__init__()
    
    def cadastrar(self, nome, usuario, cpf, telefone, senha):
        userModel = Usuario(nome=nome, usuario=usuario, cpf=cpf, telefone=telefone, senha=senha)
        
        if self.buscar_usuario('cpf', cpf):
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
    
    def buscar_usuario(self, campo, valor):
        userModel = Usuario.begin_search()
        userModel += Usuario.and_search(campo, valor, '=', operador_logico=False)
        
        return self.bd.execute_query(userModel)
    
    
    def listar_todos(self):
        return self.bd.execute_query