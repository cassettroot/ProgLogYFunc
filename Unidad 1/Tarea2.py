asistencias = [
    ("Matemáticas", "Juan", "2024-09-01"),
    ("Matemáticas", "Ana", "2024-09-01"),
    ("Física", "Juan", "2024-09-01"),
    ("Matemáticas", "Juan", "2024-09-02"),
    ("Física", "Ana", "2024-09-02")
]

alumnos_por_asignatura = {}

dias_por_alumno = {} 
conteo_asistencias = {} 

for asignatura, alumno, fecha in asistencias:
    if asignatura not in alumnos_por_asignatura:
        alumnos_por_asignatura[asignatura] = set()
    alumnos_por_asignatura[asignatura].add(alumno)
    
    if alumno not in dias_por_alumno:
        dias_por_alumno[alumno] = set()
    dias_por_alumno[alumno].add(fecha)
    
    conteo_asistencias[alumno] = conteo_asistencias.get(alumno, 0) + 1

dias_totales = {alumno: len(fechas) for alumno, fechas in dias_por_alumno.items()}
mejor_estudiante = max(conteo_asistencias, key=conteo_asistencias.get)

print(f"Alumnos por asignatura: {alumnos_por_asignatura}")
print(f"Días distintos asistidos: {dias_totales}")
print(f"Alumno con más asistencias totales: {mejor_estudiante} ({conteo_asistencias[mejor_estudiante]})")