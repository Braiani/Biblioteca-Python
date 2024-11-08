class Usuario:
    MAX_EMPRESTIMO = 5

    def __init__(self, nome, cpf,telefone) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.livros = []
    
    def create(self):
        return f'insert into usuario(nome,cpf,telefone) values ("{self.nome}", "{self.cpf}", "{self.telefone}");'
    
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