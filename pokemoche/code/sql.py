import sqlite3

class SQL:
    def __init__(self):
        self.connection = sqlite3.connect("")
        self.cursor = self.connection.cursor()

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.cursor

    def select(self,table: str, columns: list[str], where: str = None,order: str = None,limit: int =None) -> list[tuple]:
        query: str = f"SELECT{'.'}