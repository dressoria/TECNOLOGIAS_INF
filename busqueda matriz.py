

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None  # Si el valor no se encuentra

# Definir una matriz de ejemplo
matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

valor_a_buscar = 5  # Cambia este valor para buscar otros números
resultado = buscar_valor(matriz, valor_a_buscar)

if resultado:
    print(f"Valor {valor_a_buscar} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor_a_buscar} no encontrado en la matriz.")
