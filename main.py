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

# Elegir la base de datos
db_ecommerce_marketing = client["ecommerce_marketing"]

# Coleccion Clientes
coleccion_clientes = db_ecommerce_marketing["clientes"]

# Coleccion Pedidos
coleccion_pedidos = db_ecommerce_marketing["pedidos"]

# Poblar coleccion Clientes
def insercion_inicial_coleccion_clientes() -> None:
    respuesta = coleccion_clientes.insert_many(
        [
            {
                "nombre": "Laura Martínez",
                "email": "laura.martinez@gmail.com",
                "fecha_registro": "2026-01-15T10:30:00Z",
                "direccion": "Av. Providencia 1234, Santiago",
                "telefono": "+56 9 8123 4567"
            },
            {
                "nombre": "Carlos Rojas",
                "email": "carlos.rojas@hotmail.com",
                "fecha_registro": "2025-09-22T14:10:00Z",
                "direccion": "Calle Los Aromos 456, Valparaíso",
                "telefono": "+56 9 7234 5678"
            },
            {
                "nombre": "Fernanda Silva",
                "email": "fernanda.silva@gmail.com",
                "fecha_registro": "2024-03-05T09:45:00Z",
                "direccion": "Pasaje Las Rosas 789, Concepción",
                "telefono": "+56 9 6345 6789"
            },
            {
                "nombre": "Javier Torres",
                "email": "javier.torres@outlook.com",
                "fecha_registro": "2026-04-18T16:20:00Z",
                "direccion": "Av. Alemania 321, Temuco",
                "telefono": "+56 9 5456 7890"
            },
            {
                "nombre": "Camila Soto",
                "email": "camila.soto@gmail.com",
                "fecha_registro": "2025-12-02T11:00:00Z",
                "direccion": "Calle San Martín 654, La Serena",
                "telefono": "+56 9 4567 8901"
            },
            {
                "nombre": "Matías Herrera",
                "email": "matias.herrera@yahoo.com",
                "fecha_registro": "2023-07-11T13:25:00Z",
                "direccion": "Av. Brasil 987, Antofagasta",
                "telefono": "+56 9 3678 9012"
            },
            {
                "nombre": "Valentina Fuentes",
                "email": "valentina.fuentes@gmail.com",
                "fecha_registro": "2026-02-28T08:15:00Z",
                "direccion": "Camino El Alba 147, Rancagua",
                "telefono": "+56 9 2789 0123"
            },
            {
                "nombre": "Diego Morales",
                "email": "diego.morales@empresa.cl",
                "fecha_registro": "2022-10-09T17:40:00Z",
                "direccion": "Calle Maipú 258, Talca",
                "telefono": "+56 9 1890 1234"
            },
            {
                "nombre": "Paula Contreras",
                "email": "paula.contreras@gmail.com",
                "fecha_registro": "2025-06-20T12:05:00Z",
                "direccion": "Av. Costanera 369, Puerto Montt",
                "telefono": "+56 9 9001 2345"
            },
            {
                "nombre": "Andrés Vega",
                "email": "andres.vega@icloud.com",
                "fecha_registro": "2024-11-30T15:55:00Z",
                "direccion": "Pasaje Los Pinos 741, Chillán",
                "telefono": "+56 9 8111 2222"
            }
        ]
    )

    print(respuesta)

# Poblar coleccion Pedidos
def insercion_inicial_coleccion_pedidos() -> None:
    respuesta = coleccion_pedidos.insert_many(
        [
            {
                "cliente_id": 1,
                "fecha_pedido": "2026-02-10T10:00:00Z",
                "monto_total": 245.90,
                "productos": [
                {
                    "producto_id": 101,
                    "cantidad": 1,
                    "precio": 120.00
                },
                {
                    "producto_id": 205,
                    "cantidad": 2,
                    "precio": 62.95
                }
                ]
            },
            {
                "cliente_id": 2,
                "fecha_pedido": "2025-10-01T13:30:00Z",
                "monto_total": 89.50,
                "productos": [
                {
                    "producto_id": 302,
                    "cantidad": 1,
                    "precio": 89.50
                }
                ]
            },
            {
                "cliente_id": 3,
                "fecha_pedido": "2023-04-15T09:20:00Z",
                "monto_total": 560.00,
                "productos": [
                {
                    "producto_id": 101,
                    "cantidad": 2,
                    "precio": 180.00
                },
                {
                    "producto_id": 410,
                    "cantidad": 1,
                    "precio": 200.00
                }
                ]
            },
            {
                "cliente_id": 4,
                "fecha_pedido": "2026-05-03T18:45:00Z",
                "monto_total": 720.35,
                "productos": [
                {
                    "producto_id": 508,
                    "cantidad": 1,
                    "precio": 450.35
                },
                {
                    "producto_id": 207,
                    "cantidad": 3,
                    "precio": 90.00
                }
                ]
            },
            {
                "cliente_id": 5,
                "fecha_pedido": "2026-01-20T11:10:00Z",
                "monto_total": 135.75,
                "productos": [
                {
                    "producto_id": 101,
                    "cantidad": 1,
                    "precio": 135.75
                }
                ]
            },
            {
                "cliente_id": 6,
                "fecha_pedido": "2023-11-22T16:05:00Z",
                "monto_total": 42.99,
                "productos": [
                {
                    "producto_id": 601,
                    "cantidad": 1,
                    "precio": 42.99
                }
                ]
            },
            {
                "cliente_id": 7,
                "fecha_pedido": "2026-03-14T12:35:00Z",
                "monto_total": 980.00,
                "productos": [
                {
                    "producto_id": 305,
                    "cantidad": 2,
                    "precio": 250.00
                },
                {
                    "producto_id": 412,
                    "cantidad": 4,
                    "precio": 120.00
                }
                ]
            },
            {
                "cliente_id": 8,
                "fecha_pedido": "2024-08-19T19:00:00Z",
                "monto_total": 310.40,
                "productos": [
                {
                    "producto_id": 208,
                    "cantidad": 1,
                    "precio": 310.40
                }
                ]
            },
            {
                "cliente_id": 9,
                "fecha_pedido": "2025-07-08T15:25:00Z",
                "monto_total": 515.20,
                "productos": [
                {
                    "producto_id": 101,
                    "cantidad": 1,
                    "precio": 215.20
                },
                {
                    "producto_id": 509,
                    "cantidad": 2,
                    "precio": 150.00
                }
                ]
            },
            {
                "cliente_id": 10,
                "fecha_pedido": "2023-01-30T08:50:00Z",
                "monto_total": 155.00,
                "productos": [
                {
                    "producto_id": 706,
                    "cantidad": 5,
                    "precio": 31.00
                }
                ]
            },
            {
                "cliente_id": 1,
                "fecha_pedido": "2023-09-12T14:15:00Z",
                "monto_total": 75.60,
                "productos": [
                {
                    "producto_id": 333,
                    "cantidad": 2,
                    "precio": 37.80
                }
                ]
            },
            {
                "cliente_id": 2,
                "fecha_pedido": "2026-04-09T10:40:00Z",
                "monto_total": 640.90,
                "productos": [
                {
                    "producto_id": 101,
                    "cantidad": 3,
                    "precio": 120.00
                },
                {
                    "producto_id": 804,
                    "cantidad": 1,
                    "precio": 280.90
                }
                ]
            },
            {
                "cliente_id": 5,
                "fecha_pedido": "2025-12-18T17:30:00Z",
                "monto_total": 98.00,
                "productos": [
                {
                    "producto_id": 212,
                    "cantidad": 2,
                    "precio": 49.00
                }
                ]
            },
            {
                "cliente_id": 7,
                "fecha_pedido": "2023-06-25T20:10:00Z",
                "monto_total": 430.00,
                "productos": [
                {
                    "producto_id": 610,
                    "cantidad": 1,
                    "precio": 430.00
                }
                ]
            },
            {
                "cliente_id": 9,
                "fecha_pedido": "2026-05-28T09:05:00Z",
                "monto_total": 110.30,
                "productos": [
                {
                    "producto_id": 715,
                    "cantidad": 1,
                    "precio": 110.30
                }
                ]
            }
            ]
    )

    print(respuesta)

# Ejecución de insercion inicial
# insercion_inicial_coleccion_clientes()
# insercion_inicial_coleccion_pedidos()

documentos_clientes = coleccion_clientes.find({},{"_id": 1})
documentos_pedidos = coleccion_pedidos.find({},{"_id": 1})

print("Documentos de la coleccion Clientes")
for documento in documentos_clientes:
    print(documento)

print("Documentos de la coleccion Pedidos")
for documento in documentos_pedidos:
    print(documento)
