class Vehiculo:
    def __init__(self, matricula, padron, persona) -> None:
        self._matricula = matricula
        self._padron = padron
        self._persona = persona
        self._multa = []
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    
    @property
    def padron(self):
        return self._padron
    
    @padron.setter
    def padron(self, padron):
        self._padron = padron
    
    @property
    def persona(self):
        return self._persona
    
    @persona.setter
    def persona(self, persona):
        self._persona = persona
    
    @property
    def multa(self):
        return self._multa
    
    @multa.setter
    def multa(self, multa):
        self._multa = multa