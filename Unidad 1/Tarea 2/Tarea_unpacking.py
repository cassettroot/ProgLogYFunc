estudiantes = [
    ("Ana", 85, 90, 78, 92),
    ("Luis", 88, 76, 95),
    ("Carlos", 100, 98),
    ("María", 70, 80, 75, 85, 90)
]

resultados = {}

for estudiante in estudiantes:
    nombre, *calificaciones = estudiante   # unpacking extendido
    
    promedio = sum(calificaciones) / len(calificaciones)
    max_cal = max(calificaciones)
    min_cal = min(calificaciones)
    
    resultados[nombre] = {
        "promedio": promedio,
        "max": max_cal,
        "min": min_cal
    }

mejor_estudiante, datos = max(
    resultados.items(),
    key=lambda item: item[1]["promedio"]
)

print("Resultados:", resultados)
print("Mejor estudiante:", mejor_estudiante, datos)
