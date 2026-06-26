from pymongo import MongoClient

class Database:
    def __init__(self, uri, db):
        self.client = MongoClient(uri)
        self.status = False
        self.ping_admin()
        self.db = self.client[db]

    def ping_admin(self):
        try:
            print("Database> Estableciendo conexión...⏳")
            self.client.admin.command("ping")
            self.status = True
            print("Database> Conexión establecida 😊")
        except:
            print("Database> ❌ ERROR EN LA CONEXIÓN")