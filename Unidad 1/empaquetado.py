"""
datos=[1,2,3,4,5]
print(f"Arreglo original : {datos}")
copia_datos = datos
print(f"Lista 2 : {copia_datos}")
copia_datos.append(6)
print(f"Lista 2 nueva : {copia_datos}")
print(f"lista original : {datos}")
"""
#
datos = [1,2,3,4,5]
print(f"Lista original : {datos}")
#Forma adecuada de hacer una copia de una lista con desempaquetado
copia_datos=[*datos]
#impresion de una lista con desempaquetado
print(*datos)
print(f"Lista 2 : {copia_datos}")
copia_datos.append(6)
print(f"lista original : {datos}")
print(f"lista 2 {id(copia_datos)} Contenido : {copia_datos}")

def impresion_nombres(*nombres):
    print(f"los nombres son : {nombres}")
    #desempacar
    print(f"los nombres son : ",*nombres)
# se convierten en tuplas 
impresion_nombres("diego","carlos","ana")


#recibir un diccionario, no una lista
def impresion_datos(**data):
    print(f"los datos son : {data}")
#impresion diccionario
impresion_datos(nombre="carlos",tel=123456,carrera="sistemas")
diccionario_datos = {"marca":"DELL","modelo":"z7080","fecha":"hoy"}
#desempaquetado doble **
impresion_datos(**diccionario_datos)
copia_diccionario={**diccionario_datos}
impresion_datos(**copia_diccionario)