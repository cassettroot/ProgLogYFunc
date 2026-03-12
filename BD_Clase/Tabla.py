class Tabla:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__datos = []
        self.__id = 0

    def mostrarTodos(self):
        print(f"Datos tabla {self.__nombre}: {self.__datos}")

    def __incrementoId(self):
        self.__id += 1

    def insercion(self, datos):
        self.__incrementoId()
        contenido = {**datos}
        contenido['id'] = self.__id
        self.__datos.append(contenido)
        print("Los datos fueron añadidos".center(50, "-"), end="\n\n")

    def busquedaCampo(self, campo, valor, cantidad=0):
        encontrado = False

        if campo in self.__datos[0].keys():

            for registro in self.__datos:

                if registro[campo] == valor:
                    encontrado = True
                    print(registro)

                    if not cantidad:
                        break

            if not encontrado:
                print("No se localizo el registro!")

        else:
            print(f"El campo {campo} no existe")

    def editar(self, datos):
        encontrado = False
        data = {**datos}
        
        if not "id" in data.keys():
            print("ID no proporcionados")
            return False

        for posicion in range(len(self.__datos)):

            if self.__datos[posicion]['id'] == id:
                for campoEdicion,valorNuevo in data.items():
                    if campoEdicion == "id"
                        continue
                
                self.__datos[posicion][campoEdicion] = valorNuevo
                print("Registro actualizado!")
                encontrado = True
                break

        if not encontrado:
            print("Registro no localizado!")

    def eliminar(self, id: int = 0):

        for posicion in range(len(self.__datos)):

            if self.__datos[posicion]['id'] == id:

                self.__datos.pop(posicion)
                print("Registro eliminado")
                break