# fecha es el año completo
class Vacuna:
    def __init__(self, identificador, fecha, efectos_secundarios, doctor) -> None:
        self._identificador = identificador
        self._fecha = fecha
        self.efectos_secundarios = efectos_secundarios
        self._doctor = doctor
    
    @property
    def identificador(self):
        return self._identificador
    
    @identificador.setter
    def identificador(self, identificador):
        self._identificador = identificador
    
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha
    
    @property
    def efectos_secundarios(self):
        return self._efecto_secundarios
    
    @efectos_secundarios.setter
    def efectos_secundarios(self, efecto_secundarios):
        self._efecto_secundarios = efecto_secundarios
    
    @property
    def doctor(self):
        return self._doctor
    
    @doctor.setter
    def doctor(self, doctor):
        self._doctor = doctor