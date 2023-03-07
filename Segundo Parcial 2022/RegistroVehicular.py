from exceptions.InformacionInvalida import InformacionInvalida

from entities.Persona import Persona
from entities.Vehiculo import Vehiculo

class RegistroVehicular:
    def __init__(self) -> None:
        self._personas = []
        self._vehiculos = []
    
    @property
    def personas(self):
        return self._personas
    
    @personas.setter
    def personas(self, personas):
        self._personas = personas
    
    @property
    def vehiculos(self):
        return self._vehiculos
    
    @vehiculos.setter
    def vehiculos(self, vehiculos):
        self._vehiculos = vehiculos
    
    def registro_persona(self, cedula):
        if cedula is None:
            raise InformacionInvalida("Cedula Invalida")
        self._personas.append(Persona(cedula))
    
    def registro_vehicular(self, matricula, nro_padron, cedula_titular):
        existe_persona = False
        ret = False
        
        for persona in self._personas:
            if persona.cedula == cedula_titular:
                if persona.libreta_suspendida:
                    ret = True
                existe_persona = True
        
        if not existe_persona:
            self.registro_persona(cedula_titular)
            ret = True
        
        if ret:
            self._vehiculos.append(Vehiculo(matricula, nro_padron, cedula_titular))
        
        return ret
        

if __name__ == '__main__':
    
    registro1 = RegistroVehicular()
    
    print(registro1.registro_vehicular(107, 207.0, 53636064))
    print()