from Pelicula import Pelicula
from Tabla import Tabla


def editar_pelicula(tablaPeliculas):
    try:
        id_editar = int(input("Ingrese el id de la película que desea editar: "))
    except ValueError:
        print("Id inválido")
        return

    print("¿Cómo desea editar?")
    print("1. Editar un solo campo")
    print("2. Editar todos los campos")
    modo = input("Seleccione una opción (1-2): ")

    if modo == "1":
        print("¿Qué campo desea editar?")
        print("1. titulo")
        print("2. genero")
        print("3. descripcion")
        print("4. director")
        opcion = input("Seleccione una opción (1-4): ")

        mapa_campos = {
            "1": "titulo",
            "2": "genero",
            "3": "descripcion",
            "4": "director",
        }

        campo = mapa_campos.get(opcion)
        if not campo:
            print("Opción no válida")
            return

        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
        tablaPeliculas.editar(id_editar, campo, nuevo_valor)

    elif modo == "2":
        print("Deje en blanco cualquier campo que no quiera modificar.")
        nuevo_titulo = input("Nuevo titulo: ")
        nuevo_genero = input("Nuevo genero: ")
        nuevo_descripcion = input("Nueva descripcion: ")
        nuevo_director = input("Nuevo director: ")

        if nuevo_titulo:
            tablaPeliculas.editar(id_editar, "titulo", nuevo_titulo)
        if nuevo_genero:
            tablaPeliculas.editar(id_editar, "genero", nuevo_genero)
        if nuevo_descripcion:
            tablaPeliculas.editar(id_editar, "descripcion", nuevo_descripcion)
        if nuevo_director:
            tablaPeliculas.editar(id_editar, "director", nuevo_director)
    else:
        print("Opción no válida")


if __name__ == "__main__":
    print("=====Cineteca=====".center(60, "-"))


    tablaPeliculas = Tabla("Peliculas")


    while True:
        print("\nMenú Principal")
        print("Por favor ingresa mediante numero la opcion deseada")
        print("1. Ver todas las películas")
        print("2. Agregar nueva película")
        print("3. Buscar películas")
        print("4. Editar película")
        print("5. Ver historial de cambios")
        print("6. Eliminar pelicula")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            tablaPeliculas.mostrarTodos()
        elif opcion == "2":
            titulo = input("Título: ")
            genero = input("Género: ")
            descripcion = input("Descripción: ")
            director = input("Director: ")
            nueva = Pelicula(titulo, genero, descripcion, director)
            tablaPeliculas.insercion(nueva.info())
        elif opcion == "3":
            print("Opciones de búsqueda:")
            print("1. Títulos que empiecen con un texto")
            
            sub = input("Ingrese el numero, por favor , 1: ")
            texto = input("Ingrese el texto a buscar: ")

            if sub == "1":
                tablaPeliculas.busquedaCampoParcial("titulo", texto, "empieza")
            elif sub == "2":
                tablaPeliculas.busquedaCampoParcial("titulo", texto, "contiene")
            else:
                print("Opción no válida")
        elif opcion == "4":
            editar_pelicula(tablaPeliculas)
        elif opcion == "5":
            tablaPeliculas.mostrarHistorial()
        elif opcion == "7":
            print("Saliendo...")
            break
        elif opcion == "6":
            try:
                id_eliminar = int(input("Ingrese el id de la película a eliminar: "))
                tablaPeliculas.eliminar(id_eliminar)
            except ValueError:
                print("Id inválido")
        else:
            print("Opción no válida")