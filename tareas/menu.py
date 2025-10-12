# Ejemplo para recibir un nombre
nombre = input("Por favor, introduce tu nombre: ")
print("Hola, " + nombre + "!")

# Ejemplo para recibir un número (que será interpretado como texto inicialmente)
edad_str = input("Introduce tu edad: ")
edad_num = int(edad_str) # Convertimos la cadena a un número entero
print("En 10 años tendrás", edad_num + 10, "años.")