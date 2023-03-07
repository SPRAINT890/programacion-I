from entities.Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, esta_vacunado, raza) -> None:
        super().__init__(nombre, esta_vacunado)
        self._raza = raza
    
    @property
    def raza(self):
        return self._raza
    
    @raza.setter
    def raza(self, raza):
        self._raza = raza