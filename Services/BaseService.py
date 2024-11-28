from Config.Database import Database

class BaseService:
    def __init__(self):
        self.bd = Database()