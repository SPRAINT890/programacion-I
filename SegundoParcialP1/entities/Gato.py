from entities.Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, esta_vacunado, colores) -> None:
        super().__init__(nombre, esta_vacunado)
        self._colores = colores
    
    @property
    def colores(self):
        return self._colores
    
    @colores.setter
    def colores(self, colores):
        self._colores = colores