# Abrimos (o creamos si no existe) el archivo "my_notes.txt" en modo escritura ("w")
# Si el archivo ya existe, este modo sobrescribirá su contenido.
file = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales en el archivo.
file.write("Primera nota: Hoy estoy aprendiendo a trabajar con archivos en Python.\n")
file.write("Segunda nota: Los archivos de texto son muy útiles para guardar información.\n")
file.write("Tercera nota: Recordar siempre cerrar los archivos después de usarlos.\n")

# Cerramos el archivo para guardar los cambios
file.close()

# Abrimos el archivo en modo lectura ("r")
file = open("my_notes.txt", "r")

# Usamos readline() para leer línea por línea
print("Contenido del archivo my_notes.txt:")
linea = file.readline()
while linea:  # Mientras haya contenido
    print(linea.strip())  # strip() elimina saltos de línea extra al imprimir
    linea = file.readline()

# Cerramos el archivo después de leerlo
file.close()
