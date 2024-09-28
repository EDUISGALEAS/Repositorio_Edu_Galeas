# diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Edu Galeas",
    "edad": 35,
    "ciudad": "Guayaquil",
    "profesion": "Estudiante TIC"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "Estudiante TIC"

# Verificar si la clave "telefono" existe, si no existe agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998990101"  # Número ficticio

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario
print(informacion_personal)
