# comenzamos abriendo el archivo en modo escritura
with open('my_notes.txt', 'w') as file:
    # aqui voy a hacer las 3  líneas de texto
    file.write("Me llamo Andres y estoy en la carrera de ingeniera en Ti.\n")
    file.write("Esta es la ultima semana de clases.\n")
    file.write("la proxima vamos a dar examenes\n")

# aqui abrimos el archivo con las notas en modo lectura
with open('my_notes.txt', 'r') as file:
    # y final leemos linea a linea
    for line in file:
        print(line.strip())  # Eliminamos los saltos de línea adicionales
