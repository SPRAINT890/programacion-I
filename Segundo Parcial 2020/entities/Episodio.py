from exceptions.ContenidoInvalido import ContenidoInvalido

class Episodio:
    def __init__(self, temporada, numero, nombre) -> None:
        if temporada is None or numero is None or nombre is None:
            try:
                raise ContenidoInvalido("Este episodio tiene algun valor Invalido")
            except Exception as error :
                print(error)
        self._temporada = temporada
        self._numero = numero
        self._nombre = nombre
    
    @property
    def temporada(self):
        return self._temporada
    
    @temporada.setter
    def temporada(self, temporada):
        self._temporada = temporada
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
