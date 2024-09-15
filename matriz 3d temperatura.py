def calcular_temperatura_promedio(temperaturas, ciudades, semanas):
    """
    Calcula la temperatura promedio para cada ciudad durante el período de tiempo dado.
    
    :param temperaturas: Lista 3D con las temperaturas para cada ciudad, día y semana.
    :param ciudades: Lista con los nombres de las ciudades.
    :param semanas: Número de semanas en el período de tiempo.
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios_ciudades = {}
    
    for i in range(len(ciudades)):
        suma_temperaturas = 0
        num_dias = len(temperaturas[i])
        
        for semana in range(semanas):
            for dia in range(num_dias):
                suma_temperaturas += temperaturas[i][dia][semana]
        
        total_dias = num_dias * semanas
        promedio_ciudad = suma_temperaturas / total_dias
        promedios_ciudades[ciudades[i]] = promedio_ciudad
    
    return promedios_ciudades

# Datos de ejemplo para 3 ciudades y 4 semanas
temperaturas = [
    [   # Ciudad 1
        [30, 31, 29, 30], # Lunes
        [29, 32, 28, 30], # Martes
        [27, 33, 26, 29], # Miércoles
        [28, 30, 27, 28], # Jueves
        [26, 31, 25, 29], # Viernes
        [25, 29, 24, 28], # Sábado
        [24, 28, 23, 27]  # Domingo
    ],
    [   # Ciudad 2
        [22, 25, 20, 22], # Lunes
        [21, 24, 19, 21], # Martes
        [23, 22, 21, 20], # Miércoles
        [20, 21, 22, 23], # Jueves
        [19, 26, 20, 21], # Viernes
        [18, 27, 22, 24], # Sábado
        [17, 20, 21, 23]  # Domingo
    ],
    [   # Ciudad 3
        [31, 30, 32, 31], # Lunes
        [30, 29, 31, 30], # Martes
        [29, 28, 30, 29], # Miércoles
        [28, 27, 29, 28], # Jueves
        [27, 26, 28, 27], # Viernes
        [26, 25, 27, 26], # Sábado
        [25, 24, 26, 25]  # Domingo
    ]
]

ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
semanas = 4

# Calcular los promedios
promedios = calcular_temperatura_promedio(temperaturas, ciudades, semanas)

# Imprimir los resultados
for ciudad, promedio in promedios.items():
    print(f"Promedio para {ciudad}: {promedio:.2f}°C")
