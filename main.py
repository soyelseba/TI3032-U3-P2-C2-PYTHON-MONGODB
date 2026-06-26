import os
from dotenv import load_dotenv

import db
import models

def main():
    load_dotenv()
    MONGO_URI = os.getenv("MONGO_URI")
    client = db.Database(uri=MONGO_URI, db="TI3032_U3")

    db_ecommerce_marketing = client.db

    clientes = models.Clientes(name="clientes", db=db_ecommerce_marketing)
    pedidos = models.Pedidos(name="pedidos", db=db_ecommerce_marketing)

    clientes.clientes_en_el_ultimo_año()

if __name__ == "__main__":
    main()