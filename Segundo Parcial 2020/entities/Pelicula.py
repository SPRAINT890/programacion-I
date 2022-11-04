from entities.Contenido import Contenido
from exceptions.ContenidoInvalido import ContenidoInvalido

class Pelicula(Contenido):
    def __init__(self, nombre, genero, anio):
        if nombre is None or genero is None or anio < 1895:
            try:
                raise ContenidoInvalido("Esta Pelicula tiene algun valor Invalido")
            except Exception as error :
                print(error)
        super().__init__(nombre, genero)
        self._anio = anio
    
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio
