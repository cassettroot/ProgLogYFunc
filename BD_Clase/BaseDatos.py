from Pelicula import Pelicula
from Tabla import Tabla

print(f"Mi Gestor de Base de Datos".center(50, "*"))

pelicula1 = Pelicula("Spiderman", "Accion", "Pelicula del hombre araña", "Cesar Gomez Bolaños")
pelicula2 = Pelicula("Spiderman 2", "Accion", "Pelicula del hombre araña 2", "Cesar Gomez Bolaños")
pelicula3 = Pelicula("Spiderman 3", "Accion", "Pelicula del hombre araña 3", "Cesar Gomez Bolaños")
pelicula4 = Pelicula("Spiderman", "Accion", "Pelicula del hombre araña", "Cesar Gomez Bolaños")

tablaPeliculas = Tabla("Peliculas")

tablaPeliculas.insercion(pelicula1.info())
tablaPeliculas.insercion(pelicula2.info())
tablaPeliculas.insercion(pelicula3.info())
tablaPeliculas.insercion(pelicula4.info())

# tablaPeliculas.mostrarTodos()

tablaPeliculas.busquedaCampo("titulo", "Spiderman")
tablaPeliculas.editar(4, "titulo", "Spiderman 4")
tablaPeliculas.busquedaCampo("titulo", "Spiderman 4")
tablaPeliculas.eliminar(3)

tablaPeliculas.mostrarTodos()

#opcion es una lista la cual remplaza a un switch y al if 
#permite generar un listado de funciones mas practicos
#el nombre de la key corresponde a una funcion apartir de la instacia de clase Tabla
#no se colocan parentesis para evitar que se ejecuten solas al momento de la creacion

opciones = {
    "selectAll": tablaPeliculas.mostrarTodos,
    "insert": tablaPeliculas.insercion,
    "update": tablaPeliculas.editar,
    "delete": tablaPeliculas.eliminar,
}


#funcion de recibir datos : se encarga de recibir y procesar los datos en forma bruta
#que ingresa el usuario por terminal
#limpia y estructura la informacion
def recibirDatos(datos):
    #recibe una lista de datos
    objeto = {}
    #iteramos la informacion obtenida para estructurarla
    #individual: variable auxiliar contendra el valor en cada posicion de la lista
    #datos : es la lista que contiene la info
    for individual in datos:
        #usamos una variable temporal para separar los datos en dos posiciones
        #posicion0 : correcponde a la key
        #posiccion1 : el valor 
        #split permite dividir una cadena de texto apartir de un caracter
        #devuelve una lista :ejemplo dt = ["titulo","spider-man"]
        dt = individual.split("=")
        #utilizaremos un obejto vacio y añadimos los datos en el formato de un diccionario
        #se concatena una lista vacia para convertirla en un string (str)
        #la funcion strip, elimmin los espacions y fin de una cadena
        #al escribir objeto[""+dt(0).strip()] creaos una nueva key de manera dinamica
        #se asigna como valor la posicion 1 de la lista temporal
        objeto["" + dt[0].strip()] = dt[1]
        #ejemplo de lo que pasa ["titulo"] = "spider-man"
        #para diferenciar si los datos recibidos son para editar o insertar hacemos una validacion
        #se pregunta si la key "id" existe en la lista de keys del objeto creado anteriormente 
    if "id" in objeto.keys()
        #si la key "id" existe entonces lo que se pretende es hacer una actualizacion de datos, por ende retornaoms de manera pura el objeto
        # creado anteriormente
        return objeto
    else:
        #si el id no existe por defecto es una insercion lo que se pretende hacer
        #creamos una instancia de la clase Pelicula e incialmente sus valores
        pelicula = Pelicula(**objeto)
        #por ultimo retonamos lo que nos devuelve el metodo info, que no es mas que los datos procesados de manera adecuada
        #para la insercion
        return pelicula.info()

def menu():
    print("Sistema Gestor de Base de Datos".center(50, "-"))
    print("selectAll = mostrar todos los datos")
    print("insert = insercion ")
    print("update = actualizacion")
    print("delete = eliminacion")
    print("exit = salir del sistema")

    comando = input("Comando: ")
    comando = comando.split(",")

    if comando[0] in opciones.keys():
        if len(comando) > 1:
            data = recibirDatos(comando[1:])
            opciones[comando[0]](data)
        else:
            opciones[comando[0]]()
    elif comando[0] == "exit":
        print("Saliendo del DGBD".center(40, "-"))
        return False
    else:
        print("Comando no valido!")

    menu()

menu()