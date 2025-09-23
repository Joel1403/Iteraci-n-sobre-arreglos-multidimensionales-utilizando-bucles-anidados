# informacion_personal.py
# Tarea: Trabajando con Diccionarios en Python
# Código con comentarios en español

# 1) Crear el diccionario con las claves requeridas
informacion_personal = {
    "nombre": "Ana Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniera de Software"
}

# 2) Acceder y modificar "ciudad"
# Imprimir valor actual
print("Ciudad original:", informacion_personal["ciudad"])
# Modificar ciudad
informacion_personal["ciudad"] = "Guayaquil"
print("Ciudad modificada:", informacion_personal["ciudad"])

# 2b) Agregar/actualizar "profesion" (aunque ya existe, lo actualizamos)
informacion_personal["profesion"] = "Desarrolladora Backend"
print("Profesión actualizada:", informacion_personal["profesion"])

# 3) Verificar existencia de "telefono" y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 98 765 4321"  # número ficticio
    print("Teléfono agregado:", informacion_personal["telefono"])
else:
    print("Teléfono ya existe:", informacion_personal["telefono"])

# 4) Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Clave 'edad' eliminada.")
else:
    print("La clave 'edad' no existe, por lo que no se pudo eliminar.")

# 5) Imprimir el diccionario final
print("\nDiccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
