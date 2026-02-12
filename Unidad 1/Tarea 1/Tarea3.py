inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

cat_productos = {}
agotados = set()
total_por_categoria = {}

for item in inventario:
    prod = item["producto"]
    cat = item["categoria"]
    stk = item["stock"]
    
    if cat not in cat_productos:
        cat_productos[cat] = []
    cat_productos[cat].append(prod)
    
    if stk == 0:
        agotados.add(prod)
        
    total_por_categoria[cat] = total_por_categoria.get(cat, 0) + stk

stock_bajo = tuple(item["producto"] for item in inventario if item["stock"] < 5)

print(f"Productos por categoría: {cat_productos}")
print(f"Productos agotados: {agotados}")
print(f"Alerta stock bajo (<5): {stock_bajo}")
print(f"Unidades totales por categoría: {total_por_categoria}")