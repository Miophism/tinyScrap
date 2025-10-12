##prueba de creacion de db
##Importar dependencias mysql.connectory msqil errorcode
##Instale un lector de .env


import os
from sqlite3 import Cursor
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv 



# print("Host ",db_host)
# print("User ",db_user)
# print("Pss ",db_pss)
# print("Name ",db_name)


def getConection():
    load_dotenv()
    connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),  # el puerto debe ser un entero
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    )

    return connection
            



def create_db(db_name:str):
    try:
        conn= getConection()
        print("Conexion exitosa")
        cursor= conn.cursor()
        load_dotenv()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS`{db_name}`")
        print("Base de datos creada correctamente")
        cursor.close()
        conn.close()
        print("Conexion cerrada")
    except Exception as e :
        print("Error al conectar", e )
    
# def createTable():
#         try:
#             conn= getConection()
#             print("Conexion exitosa")
#             cursor= conn.cursor()
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS usuarios (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     nombre VARCHAR(100) NOT NULL,
#                     email VARCHAR(100) UNIQUE NOT NULL,
#                     creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                 )
#                 """)            
#             print("Tabla creada de manera exitosa")
#             cursor.close()
#             conn.close()
#         except Exception as e :
#             print("Error al crear", e )
    


# createTable()