import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv 

def getConection():
    try:
        load_dotenv()
        connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),  
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        )
        
        return connection,"Conexion exitosa"      
   
    except mysql.connector.Error as err:
        match err.errno: 
            case 1045: 
                msg="Acceso denegado, contraseña o usuario incorrectos"
            case 2003: 
                msg="No se puede conectar al servidor de la base de datos Host/puerto incorrecto"
            case 1049:
                msg="Base de datos desconocida"
            case _:
                msg=f"Error inesperado de Mysql: {err}" 
    return None, msg


            
def errorsQuery(err):
    match err.errno:
        case 1044:
            msg="Errpr: usuario no tiene permiso para crear tablas "
        case 1064:
            msg="Error: en la sintaxis de la consulta"
        case 1046:
            msg="Error: no selecciono una base de datos"
        case 1050:
            msg="Error: esta tabla ya existe"
        case 1062:
            msg="Eror: valores duplicados."
        case 1071:
            msg="Erro: clave demasiado grande para el motor de almacenamiento"
        case 1215:
            msg= "Error: fallo la creacion de una clave foranea"
        case 1364:
            msg="Error: una columna requiere un valor por defecto"
        case _:
            msg=f"Error inesperado al ejecutar la consulta: {err}"
    return False, msg


def execute(consulta, params= None):
    
    connection,msg= getConection()
    if not connection:
        return False,msg
    cursor= None
    
    if not consulta or not consulta.strip():
        return False, "Consulta vacía o inválida"


    try:
        cursor= connection.cursor()
        cursor.execute(consulta, params or ())
        connection.commit()
        return True,"Consulta ejecutada correctamente"
    except mysql.connector.Error as err:
        return errorsQuery(err);
    finally:
        if cursor:
            cursor.close()
        if connection: 
            connection.close()
            
