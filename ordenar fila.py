

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila(matriz, fila):
    if 0 <= fila < len(matriz):
        bubble_sort(matriz[fila])
    else:
        print("Índice de fila fuera de rango.")

# Definir una matriz de ejemplo
matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 1  # Cambia este valor para ordenar otra fila
ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz después de ordenar la fila:")
for fila in matriz:
    print(fila)
