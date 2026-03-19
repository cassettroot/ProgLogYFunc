# 1. ANALISIS DE CODIGO

numeros = [1, 2, 3, 4, 5]

total = 0
for i in range(len(numeros)):
    total = total + numeros[i]

print("Suma (forma original):", total)

# ¿Que hace?
# Recorre la lista usando indices y suma todos los elementos a final tenienndo 
# suma total de 15

# Problemas:
# - se podria considerar que no esta optimizado, ya que se puede escribir mas corto

# Optimizado

"""
total_manual = 0
for numero in numeros:
    total_manual += numero
print("Suma (sin indices):", total_manual)
"""


# 2. REFACTORIZACION

lista = [10, 20, 30, 40]

print("\nImpresion original:")
for i in range(len(lista)):
    print(lista[i])

# Problema:
# - Uso de indices

# Codigo refactorizado:
"""
print("\nImpresion refactorizada:")
for numero in lista:
    print(numero)
"""
# Mejora:
# - Codigo mas limpio y sobre todo mas corto


# 3. OPTIMIZACION DE CODIGO

pares = []

for i in range(1, 101):
    if i % 2 == 0:
        pares.append(i)

print("\nPares (forma original):", pares)

# Problema:
# - Se puede simplificar

# Codigo optimizado
pares_opt = [i for i in range(1, 101) if i % 2 == 0]
print("Pares (optimizado):", pares_opt)

# Mejora:
# - Menos lineas


# 4. ANALISIS DE COMPLEJIDAD

print("\nAnalisis de complejidad:")

for i in lista:
    for j in lista:
        print(i, j)

# Explicacion:
# - hay dos bucles anidados
# - se vuelve lento con listas grandes


# 5. EJERCICIO

numeros = [5, 10, 15, 20, 25]

# Funcion para promedio
def promedio(lista):
    return sum(lista) / len(lista)

# Funcion para maximo
def maximo(lista):
    return max(lista)

# Funcion para minimo
def minimo(lista):
    return min(lista)

print("\nResultados ejercicio:")
print("Promedio:", promedio(numeros))
print("Maximo:", maximo(numeros))
print("Minimo:", minimo(numeros))

# Mejora:
# - Funciones reutilizables
# - Codigo limpio