from entities.Contenido import Contenido
from exceptions.ContenidoInvalido import ContenidoInvalido

class Serie(Contenido):
    def __init__(self, nombre, genero):
        if (nombre is None or genero is None):
            try:
                raise ContenidoInvalido("Esta Serie tiene algun valor Invalido")
            except Exception as error :
                print(error)
        super().__init__(nombre, genero)
        self._episodios = []
    
    @property
    def episodios(self):
        return self._episodios

    @episodios.setter
    def episodios(self, episodios):
        self._episodios = episodios
