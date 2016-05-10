from tinydb import *


class CommonStore:
    DB_FILE_PATH = "common.db"
    db = None

    def __init__(self):
        self.db = TinyDB(self.DB_FILE_PATH)

    def store(self, tablename, key, value):
        table = self.db.table(tablename)
        table.insert({"key": key, "value": value})

    def get(self, tablename, key):
        table = self.db.table(tablename)
        return table.search(Query()["key"] == key)
