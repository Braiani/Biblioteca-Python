import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class Database:

    def __init__(self) -> None:
        self.conexao = None
        self.conector = None

    def conectar(self):
        try:
            config = self.get_info_from_env()

            if not config:
                raise Exception('Erro ao carregar variáveis de ambiente')
            
            self.conexao = mysql.connector.connect(
                host=config['host'],
                port=config['port'],
                database=config['database'],
                user=config['user'],
                password=config['password']
            )

            if not self.conexao.is_connected():
                raise Error
            
            self.conector = self.conexao.cursor()
            
        except Error as err:
            print(f'Não foi possível conectar: {err}')
        except Exception as error:
            print(f'Erro ao tentar achar o arquivo Config: {error}')
    
    @staticmethod
    def get_info_from_env():
        try:
            load_dotenv()
            return {
                'host': os.getenv('host', '10.28.2.15'),
                'port': os.getenv('port', '3306'),
                'database': os.getenv('database', 'biblioteca'),
                'user': os.getenv('user', 'suporte'),
                'password': os.getenv('password', 'suporte')
            }
        except Exception as e:
            print(f'Erro ao carregar variáveis de ambiente: {e}')
            return False

    def desconectar(self):
        if self.conexao.is_connected():
            self.conexao.close()
            self.conexao = None
            self.cursor = None

        print('Desconectado com sucesso!')
    
    def execute_query(self, query, params:None|list = None, commit:bool = False):
        try:
            self.conectar()

            cursor = self.conexao.cursor(dictionary=True)
            
            cursor.execute(query, params)
            if commit:
                self.conexao.commit()
                return cursor.rowcount
            else:
                records = cursor.fetchall()
                return records
            
        except Error as err:
            print(f'Ocorreu um erro: {err}')
            return False
        finally:
            self.desconectar()

Database.__name__ = "Database"