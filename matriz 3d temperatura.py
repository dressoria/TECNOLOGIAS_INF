# Creamos la matriz 3D para almacenar las temperaturas con los valores indicados
# dimensiones: ciudades (2), días de la semana (7), semanas (2)
temperaturas = [
    [   # Ciudad 1
        [30, 31], # Lunes (semana 1, semana 2)
        [29, 32], # Martes
        [27, 33], # Miércoles
        [28, 30], # Jueves
        [26, 31], # Viernes
        [25, 29], # Sábado
        [24, 28]  # Domingo
    ],
    [   # Ciudad 2
        [22, 25], # Lunes
        [21, 24], # Martes
        [23, 22], # Miércoles
        [20, 21], # Jueves
        [19, 26], # Viernes
        [18, 27], # Sábado
        [17, 20]  # Domingo
    ]
]

# Usamos bucles anidados para calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad1", "Ciudad2"]
semanas = 2

for i in range(len(ciudades)):
    print(f"Promedios para {ciudades[i]}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(temperaturas[i])):
            suma_temperaturas += temperaturas[i][dia][semana]
        promedio_semana = suma_temperaturas / len(temperaturas[i])
        print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")
