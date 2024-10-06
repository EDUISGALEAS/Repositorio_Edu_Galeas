# Crear el archivo
archivo = open("my_notes.txt", "w")
notas = [
    "toca ir a trabajar otra vez.\n",
    "quiero vacaciones urgente.\n",
    "FELICITAR A EDU GALEAS.\n"
]

for nota in notas:
    archivo.write(nota)

archivo.close()


# Leer y mostrar el contenido del archivo
archivo = open("my_notes.txt", "r")
linea = archivo.readline()

while linea:
    print(linea, end="")
    linea = archivo.readline()

archivo.close()





