class Tabla:
    def __init__(self, nombre):
        self._nombre = nombre
        self._datos = []
        self._id = 0
        self._historial = []

    def _agregarHistorial(self, mensaje):
        self._historial.append(mensaje)

    def mostrarTodos(self):
        print(f"Datos tabla {self._nombre}:")
        for registro in self._datos:
            print(registro)

    def _incrementoId(self):
        self._id += 1

    def insercion(self, datos: dict):
        self._incrementoId()
        contenido = dict(datos)
        contenido["id"] = self._id
        self._datos.append(contenido)
        self._agregarHistorial(f"Inserción de registro con id {self._id}: {contenido}")
        print("Los datos fueron añadidos".center(50, "-"), end="\n\n")

    def busquedaCampo(self, campo, valor, cantidad=0):
        if not self._datos:
            print("La tabla está vacía")
            return

        if campo not in self._datos[0].keys():
            print(f"El campo {campo} no existe")
            return

        encontrados = 0
        for registro in self._datos:
            if registro.get(campo) == valor:
                print(registro)
                encontrados += 1
                if cantidad != 0 and encontrados >= cantidad:
                    break

        if encontrados == 0:
            print("No se localizó el registro!")

    def editar(self, id, campo, valor):
        if not self._datos:
            print("La tabla está vacía")
            return

        if campo not in self._datos[0].keys():
            print(f"El campo {campo} no existe")
            return

        encontrado = False
        for posicion in range(len(self._datos)):
            if self._datos[posicion].get("id") == id:
                anterior = dict(self._datos[posicion])
                self._datos[posicion][campo] = valor
                self._agregarHistorial(
                    f"Edición de id {id}: campo '{campo}' de '{anterior.get(campo)}' a '{valor}'"
                )
                encontrado = True
                print("Registro actualizado")
                break
        if not encontrado:
            print("Registro no localizado!")

    def editarPorCampo(self, campo_busqueda, valor_busqueda, campo_editar, valor_nuevo):
        if not self._datos:
            print("La tabla está vacía")
            return

        if campo_busqueda not in self._datos[0].keys():
            print(f"El campo {campo_busqueda} no existe")
            return

        if campo_editar not in self._datos[0].keys():
            print(f"El campo {campo_editar} no existe")
            return

        encontrado = False
        for posicion in range(len(self._datos)):
            if self._datos[posicion].get(campo_busqueda) == valor_busqueda:
                anterior = dict(self._datos[posicion])
                self._datos[posicion][campo_editar] = valor_nuevo
                self._agregarHistorial(
                    "Edición por campo "
                    f"({campo_busqueda}='{valor_busqueda}'): campo '{campo_editar}' "
                    f"de '{anterior.get(campo_editar)}' a '{valor_nuevo}'"
                )
                encontrado = True
                print("Registro actualizado")
                break
        if not encontrado:
            print("Registro no localizado!")

    def eliminar(self, id: int = 0):
        encontrado = False
        for posicion in range(len(self._datos)):
            if self._datos[posicion].get("id") == id:
                anterior = dict(self._datos[posicion])
                del self._datos[posicion]
                self._agregarHistorial(f"Eliminación de registro con id {id}: {anterior}")
                encontrado = True
                print("Registro eliminado!")
                break
        if not encontrado:
            print("Registro no localizado!")

    def busquedaCampoParcial(self, campo, texto, modo="contiene"):
        if not self._datos:
            print("La tabla está vacía")
            return

        if campo not in self._datos[0].keys():
            print(f"El campo {campo} no existe")
            return

        texto = str(texto).lower()
        encontrados = 0

        for registro in self._datos:
            valor = str(registro.get(campo, "")).lower()
            coincide = False

            if modo == "empieza":
                coincide = valor.startswith(texto)
            else:  # contiene
                coincide = texto in valor

            if coincide:
                print(registro)
                encontrados += 1

        if encontrados == 0:
            print("No se localizó el registro!")

    def mostrarHistorial(self):
        if not self._historial:
            print("No hay cambios registrados")
            return

        print(f"Historial de cambios de {self._nombre}:")
        for item in self._historial:
            print(f"- {item}")