class Pelicula:
    def __init__(self, titulo, genero, descripcion, director):
        self._titulo = titulo
        self._genero = genero
        self._descripcion = descripcion
        self._director = director
        
    def info(self):
        return {
            "titulo": self._titulo, 
            "genero": self._genero, 
            "descripcion": self._descripcion, 
            "director": self._director
        }