class Animal:
    def __init__(self, nombre, esta_vacunado) -> None:
        self._nombre = nombre
        self._esta_vacunado = esta_vacunado
        self._vacunas = []
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def esta_vacunado(self):
        return self._esta_vacunado
    
    @esta_vacunado.setter
    def esta_vacunado(self, esta_vacunado):
        self._esta_vacunado = esta_vacunado
    
    @property
    def vacunas(self):
        return self._vacunas
    
    @vacunas.setter
    def vacunas(self, vacunas):
        self._vacunas = vacunas