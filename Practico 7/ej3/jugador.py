"""
jugador (ci, nombre, edad, años exp, posicion(base, escolta, alero, ala-pivot, pivot))
"""

class Jugador:
    def __init__(self, ci, nombre, edad, años_exp, posicion):
        self._ci = ci
        self._nombre = nombre
        self._edad = edad
        self._años_exp = años_exp
        self._posicion = posicion
    
    def __str__(self):
        return "Ci: {}, Nombre: {}, Edad: {}, Años de Exp {}, Posicion: {}".format(self.ci, self.nombre, self.edad, self.años_exp, self.posicion)
    
    @property
    def ci(self):
        return self._ci
    
    @ci.setter
    def ci(self, ci):
        self._ci = ci
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def años_exp(self):
        return self._años_exp
    
    @años_exp.setter
    def años_exp(self, años_exp):
        self._años_exp = años_exp
    
    @property
    def posicion(self):
        return self._posicion
    
    @posicion.setter
    def posicion(self, posicion):
        self._posicion = posicion

"""if __name__ == '__main__':
    j1 = Jugador("53636064", "Gaspar Morales", "19", "1", "base")
    print(j1)"""