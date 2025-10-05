import csv

# Datos para escribir en el archivo CSV
datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Ana', 30, 'Buenos Aires'],
    ['Juan', 25, 'CABA'],
    ['María', 28, 'La Plata']
]

# Abre el archivo en modo escritura ('w')
# newline='' es importante para evitar líneas en blanco adicionales en el archivo CSV
with open('datos_personas.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    # Crea un objeto writer
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribe todas las filas de la lista de datos
    escritor_csv.writerows(datos)

print("Archivo 'datos_personas.csv' creado exitosamente.")


