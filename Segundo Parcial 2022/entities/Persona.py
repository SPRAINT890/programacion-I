class Persona:
    def __init__(self, cedula) -> None:
        self._cedula = cedula
        self._libreta_suspendida = False
        self._vehiculo = []
    
    @property
    def cedula(self):
        return self._cedula
    
    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula
    
    @property
    def libreta_suspendida(self):
        return self._vehiculo
    
    @libreta_suspendida.setter
    def libreta_suspendida(self, libreta_suspendida):
        self._vehiculo = libreta_suspendida
    
    @property
    def vehiculo(self):
        return self._vehiculo
    
    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self._vehiculo = vehiculo