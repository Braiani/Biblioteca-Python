class Usuario:
    MAX_EMPRESTIMO = 5

    def __init__(self, nome, cpf,telefone, senha) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
        self.livros = []
    
    def create(self):
        return f'insert into usuario(nome,cpf,telefone,senha) values ("{self.nome}", "{self.cpf}", "{self.telefone}", "{self.senha}");'
    
    @staticmethod
    def search(coluna, valor, operador = "="):
        consulta = valor
        if operador == "like":
            consulta = f"%{valor}%"
        return f'select * from usuario where {coluna} {operador} "{consulta}";'
    
    @staticmethod
    def update(coluna, novo_valor, where):
        return f'update usuario set {coluna} = "{novo_valor}" where {coluna} = "{where}";'
    
    @staticmethod
    def delete(cpf):
        return f'delete from usuario where cpf = {cpf}'