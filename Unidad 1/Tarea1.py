ventas = [
    ("Ana", "Enero", "Laptop", 2, 15000),
    ("Luis", "Enero", "Mouse", 10, 250),
    ("Ana", "Febrero", "Laptop", 1, 15000),
    ("Luis", "Febrero", "Teclado", 5, 800),
    ("Ana", "Enero", "Mouse", 3, 250)
]

ingresos_empleado = {}
productos_unicos = set()
ingresos_mes = {}

for empleado, mes, producto, cantidad, precio in ventas:
    subtotal = cantidad * precio
    
    ingresos_empleado[empleado] = ingresos_empleado.get(empleado, 0) + subtotal
    
    productos_unicos.add(producto)
    
    ingresos_mes[mes] = ingresos_mes.get(mes, 0) + subtotal

mejor_empleado = max(ingresos_empleado, key=ingresos_empleado.get)

print(f"Ingresos por empleado: {ingresos_empleado}")
print(f"Productos únicos: {productos_unicos}")
print(f"Ingresos por mes: {ingresos_mes}")
print(f"Empleado estrella: {mejor_empleado} con ${ingresos_empleado[mejor_empleado]}")

