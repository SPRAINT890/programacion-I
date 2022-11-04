from abc import ABC, abstractmethod

class Contenido(ABC):
    def __init__(self, nombre, genero):
        self._nombre = nombre
        self._genero = genero
    
    def es_recomendado(slef, generos_vistos):
        pass
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero
