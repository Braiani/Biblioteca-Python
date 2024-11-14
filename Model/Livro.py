class Livro:
    def __init__(self, titulo,autor,genero, codigo, status = 'Disponível') -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.status = status
    
    def create(self):
        return f'insert into livro(titulo, autor, genero, status, codigo) values ("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", {self.codigo});'
    
    @staticmethod
    def search(coluna, valor, operador = "="):
        consulta = valor
        if operador == "like":
            consulta = f"%{valor}%"
        return f'select * from livro where {coluna} {operador} "{consulta}";'
    
    @staticmethod
    def update(coluna, novo_valor, identificador, where):
        return f'update livro set {coluna} = "{novo_valor}" where {identificador} = "{where}";'
    
    @staticmethod
    def delete(coluna, valor):
        return f'delete from livro where {coluna} = {valor}'