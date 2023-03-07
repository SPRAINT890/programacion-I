class Doctor:
    def __init__(self, nombre_completo, edad, calificacion) -> None:
        self._nombre_completo = nombre_completo
        self._edad = edad
        self._calificacion = calificacion
    
    @property
    def nombre_completo(self):
        return self._nombre_completo
    
    @nombre_completo.setter
    def nombre_completo(self, nombre_completo):
        self._nombre_completo = nombre_completo
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def calificacion(self):
        return self._calificacion
    
    @calificacion.setter
    def calificacion(self, calificacion):
        self._calificacion = calificacion