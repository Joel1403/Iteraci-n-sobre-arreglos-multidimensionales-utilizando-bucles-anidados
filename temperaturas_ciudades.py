# temperaturas_ciudades.py
# Código listo para copiar y pegar directamente en GitHub

# Lista de ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Número de semanas
num_semanas = 2

# Matriz 3D de temperaturas: [ciudad][semana][día]
matriz_temperaturas = [
    [   # Quito
        [20, 21, 19, 22, 20, 21, 19],   # Semana 1
        [21, 22, 20, 23, 21, 22, 20]    # Semana 2
    ],
    [   # Guayaquil
        [28, 27, 29, 30, 28, 27, 29],   # Semana 1
        [29, 28, 30, 31, 29, 28, 30]    # Semana 2
    ],
    [   # Cuenca
        [16, 17, 15, 18, 16, 17, 15],   # Semana 1
        [17, 18, 16, 19, 17, 18, 16]    # Semana 2
    ]
]

# Mostrar temperaturas completas
print("Temperaturas diarias por ciudad y semana:")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for j in range(num_semanas):
        print(f"  Semana {j+1}: {matriz_temperaturas[i][j]}")

# Calcular y mostrar promedios semanales por ciudad
print("\nPromedios semanales por ciudad:")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for j in range(num_semanas):
        suma = 0
        for k in range(len(dias_semana)):
            suma += matriz_temperaturas[i][j][k]
        promedio = suma / len(dias_semana)
        print(f"  Semana {j+1}: {promedio:.2f} °C")
