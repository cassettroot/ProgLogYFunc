# Comentarios
# str es una ayuda visual para el programador str = string int = entero

texto :str = "cadena de texto"
entero :int = 10
flotante :float = 1.5
booleano :bool = True

#impresion de texto
print("hola mundo")

#impresion de variables
print(texto,entero)

#impresion con escape de variable
print(f'Este es el valor de una variable {flotante}')
print('Este es un texto ',booleano)

#funciones adicionales de print
print("Menu de usuario".center(50,"-"))
print("Texto de prueba ",end=".")
print("Texto de prueba 2",end="\n")
print("Texto de prueba 3",end="\n\n")

#impresion de tipo de dato

print(type(texto))
print(type(entero))
print(type(flotante))
print(type(booleano))

#impresion de memoria
print(id(texto))
print(id(entero))
print(id(flotante))
print(id(booleano))

#estructura de control
if 0 < entero < 100:
    print("Estas dentro del rango")
elif entero < 0:
    print("Es negativo")
else:
    print("Es menor ")
    
#Ciclo de repeticion
#     (inicio, limite, incremento)
for i in range(5,30,5):
    print(i,end=(","))

for letra in texto:
    print(letra)

#ciclo de repeticion while
"""
contador = 0
while True:
    print("Bucle infinito")
    contador += 1
    if contador <= 5:
        break

"""
#lista

lista_frutas :list= []
lista_alterna:list = list ()

#impresion de lista

print(lista_frutas)
print(lista_alterna)

#impresion de tipo de dato

print(type(lista_frutas))
print(type(lista_alterna))

#funciones de las listas

lista_frutas.append("manzana")
lista_frutas.append("mango")
lista_frutas.append("mandarina")

#cuantos elementos tiene

print(len(lista_frutas))

#impresion de lista

print(lista_frutas)

# insercion de un nuevo elemento con la funcion 'insert'
# requiere una posicion y valor 

lista_frutas.insert(1,"pera")
print(lista_frutas)

#eliminar el ultimo registro de una lsita con la funcion pop()

lista_frutas.pop()
print(lista_frutas)

#eliminar un elemento de la lista con la funcion remove

lista_frutas.remove("manzana")
print(lista_frutas)

#limpiar una lista con la funcion clear()

#lista_frutas.clear()
print(lista_frutas)

#como elimnar una lista 'del' esto hace que se elimine una lista

#del lista_frutas

print("lista frutas ...")

#como recorrer en lista

for i in lista_frutas:
    print(i,end=",")

print("")
#recorrer una lsita con for normal
for i in range(len(lista_frutas)):
    print(lista_frutas[i])
    
#impresion posicion

print(lista_frutas[0])

#cambiar el valor de la posicion

lista_frutas[1] = "naranja"
print(lista_frutas)

#como saltar o iniciar desde una posicion hasta el final.............

print("")

lista_frutas.append("manzana")
lista_frutas.append("mango")
lista_frutas.append("mandarina")
# en la primera posicion decimos que inicie desde la posicion 1 hasta la fruta 3
print(lista_frutas)
print(lista_frutas[1:3])

#tuplas

tuplas_nombre = ("carlos","alberto","diego","ana")
tuplas_alterna = tuple()
#imprimir tipo de datos
print(type(tuplas_nombre))
print(type(tuplas_alterna))
#imprimir por total
print(tuplas_nombre)
#imprimir por posicion
print(tuplas_nombre[2])
#imprimir por iteracion
for nombre in tuplas_nombre:
    print(nombre)
    
#borrar tuplas
# del tuplas_nombre
print(tuplas_nombre)

#como agregar a mas personas con for
lista_nombres=[]
for i in tuplas_nombre:
    lista_nombres.append(i)
print(tuplas_nombre)
lista_nombres.append("jorge")
lista_nombres.append("diana")
print("esto es una lista")
print(lista_nombres)
tuplas_nombre=tuple(lista_nombres)
print("esto es una tupla")
print(tuplas_nombre)

#coleccion set

coleccion ={'tierra','marte','jupiter','saturno','pluton'}
coleccion_alterna=set()

#impresion de tipo de dato

print(type(coleccion))
print(type(coleccion_alterna))
#impresion
print(coleccion)

#añade un elemento a la coleccion
coleccion.add('mercurio')
print(coleccion)

#sirve para añadir elementos aparatir de otra estructura de datos

coleccion.update(lista_frutas)
coleccion.update(tuplas_nombre)
print(coleccion)

#elimina un elemento de la coleccion, si no existe el elemento da error

coleccion.remove('pluton')
print(coleccion)

#descarta un elemento, si no existe da error

coleccion.discard('pluton')
print(coleccion)

#limpia todo el contenido
coleccion.clear()
print(coleccion)

##Diccionarios

diccionario = {"nombre":"carlos","carrera":"sistemas"}
diccionario_alterno = dict()

#impresion de tipo

print(type(diccionario))
print(type(diccionario_alterno))

#impresion general
print(diccionario)
print(diccionario["carrera"])

#editar una key del diccionario

diccionario["nombre"] = "Carlos"
print(diccionario)

#añadir nuevos elementos
diccionario["semestre"]=8
print(diccionario)

#clear limpia todo
#pop borra el ultimo
#update

#
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

for key,valor in diccionario.items():
    print(f"la key es : {key}, el valor es : {valor}" )
######################################   
#declarar o definir una funcion 

def test():
    print("Impresion de funcion")
    
#Invocacion de una funcion

test()
#Funcion con argumentos

#def test2 (nombre):
#    print(f"Hola ,{nombre}")
#test2("Carl")

def test2 (nombre = "Desconocido", carrera = "Sin carrera"):
    print(f"Hola ,{nombre} tu carrera es : {carrera}")
test2(carrera="sistemas")