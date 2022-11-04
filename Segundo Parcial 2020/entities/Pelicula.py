from entities.Contenido import Contenido
from exceptions.ContenidoInvalido import ContenidoInvalido

class Pelicula(Contenido):
    def __init__(self, nombre, genero, anio):
        if len(nombre) == 0 or len(genero) == 0 or anio < 1895:
            raise ContenidoInvalido("Esta Pelicula tiene algun valor Invalido")
        super().__init__(nombre, genero)
        self._anio = anio
    
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio
