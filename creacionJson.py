import json

datos_python = {
    "nombre": "Ejemplo",
    "edad": 30,
    "ciudades": ["Madrid", "París"]
}

nombre_archivo = "datos.json"

with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
    json.dump(datos_python, archivo_json, indent=4)