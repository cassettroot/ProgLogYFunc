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

opciones = {
    "selectAll": tablaPeliculas.mostrarTodos,
    "insert": tablaPeliculas.insercion,
    "update": tablaPeliculas.editar,
    "delete": tablaPeliculas.eliminar,
}

def recibirDatos(datos):
    objeto = {}
    edicion = False
    for individual in datos:
        dt = individual.split("=")
        objeto["" + dt[0].strip()] = dt[1]
    pelicula = Pelicula(**objeto)
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