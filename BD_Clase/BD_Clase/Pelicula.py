class Pelicula:

    def __init__(self, titulo, genero, descripcion, director):
        self.__titulo = titulo
        self.__genero = genero
        self.__descripcion = descripcion
        self.__director = director
        print(f"Se creado la pelicula: {self.info()}")

    def info(self):
        return {
            "titulo": self.__titulo,
            "genero": self.__genero,
            "descripcion": self.__descripcion,
            "director": self.__director
        }