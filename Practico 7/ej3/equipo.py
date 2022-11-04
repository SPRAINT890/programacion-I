"""
equipo(nombre, lista jugadores titulares, lista jugadores suplentes, )
"""

class Equipo:
    def __init__(self, nombre, jugadores_titulares, jugadores_suplentes):
        self._nombre = nombre
        self._jugadores_titulares = jugadores_titulares
        self._jugadores_suplentes = jugadores_suplentes

    def __str__(self):
        return "Nombre: {}, Jugadores Titulares: {}, Jugadores suplentes: {}"
    
    @property
    def jugadores_suplentes(self):
        return self._jugadores_suplentes
    
    @jugadores_suplentes.setter
    def jugadores_suplentes(self, jugadores_suplentes):
        self._jugadores_suplentes = jugadores_suplentes
    
    @property
    def jugadores_titulares(self):
        return self._jugadores_titulares
    
    @jugadores_titulares.setter
    def jugadores_titulares(self, jugadores_titulares):
        self._jugadores_titulares = jugadores_titulares
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

if __name__ == '__main__':
    e1 = Equipo("MariaDB", ["Gaspar", "Fabricio", "Ignacio"], ["Lorena", "Felipe", "Joaquin"])