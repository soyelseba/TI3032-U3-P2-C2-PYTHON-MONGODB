import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

try:
    print("Estableciendo conexión...⏳")
    client.admin.command("ping")
except:
    print("❌ ERROR EN LA CONEXIÓN")
    exit(code=1)

print("Conexión establecida 😊")
db = client["ti3032_u3"]
coleccion = db["test"]