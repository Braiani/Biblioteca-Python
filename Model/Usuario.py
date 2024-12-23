class Usuario:
    MAX_EMPRESTIMO = 5

    def __init__(self, nome, usuario, cpf,telefone, senha) -> None:
        self.nome = nome
        self.usuario = usuario
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
        self.livros = []
    
    def create(self):
        return f'insert into usuario(nome,usuario,cpf,telefone,senha) values ("{self.nome}", "{self.usuario}", "{self.cpf}", "{self.telefone}", "{self.senha}");'
    
    @staticmethod
    def search_all():
        return 'select * from usuario'

    @staticmethod
    def begin_search():
        return f'select * from usuario where '

    @staticmethod
    def and_search(coluna, valor, operador = "=", operador_logico = True):
        consulta = valor
        if operador == "like":
            consulta = f"%{valor}%"
        logical = ''
        if operador_logico:
            logical = 'and'
        return f'{logical} {coluna} {operador} "{consulta}" '
    
    @staticmethod
    def or_search(coluna, valor, operador = "=", operador_logico = True):
        consulta = valor
        if operador == "like":
            consulta = f"%{valor}%"
        logical = ''
        if operador_logico:
            logical = 'or'
        return f'{logical} {coluna} {operador} "{consulta}" '
    
    @staticmethod
    def update(coluna, novo_valor, where):
        return f'update usuario set {coluna} = "{novo_valor}" where {coluna} = "{where}";'
    
    @staticmethod
    def delete(cpf):
        return f'delete from usuario where cpf = {cpf}'