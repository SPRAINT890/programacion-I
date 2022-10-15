"""
Crear una clase que represente a una persona. En ella como datos mínimos se
debe incluir el nombre, su cedula de identidad (sin dígito verificador), su
dirección y teléfono:
a. Crear un constructor para la clase que reciba los atributos de la
persona.
b. Realizar métodos getter y setter para todos los atributos de la clase. 
"""

class Persona:
    def __init__(self, nombre, ci, dir, tel, tarjeta):
        self._nombre = nombre
        self._ci = ci
        self._dir = dir
        self._tel = tel
        self._tarjeta = tarjeta
    
    @property
    def tarjeta(self):
        return self._tarjeta
    
    @tarjeta.setter
    def tarjeta(self, tarjeta):
        self._tarjeta = tarjeta
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def ci(self):
        return self._ci
    
    @ci.setter
    def ci(self, ci):
        self._ci = ci
    
    @property
    def dir(self):
        return self._dir
    
    @dir.setter
    def dir(self, dir):
        self._dir = dir
    
    @property
    def tel(self):
        return self._tel
    
    @tel.setter
    def tel(self, tel):
        self._tel = tel
    
    def __str__(self):
        return "nombre: {}, ci: {}, direccion: {}, telefono {}, tarjeta {}".format(self.nombre, self.ci, self.dir, self.tel, self.tarjeta)

"""if __name__ == '__main__':
    p1 = Persona("John Doe", "5555555", "Gral. Nariño 2388", "91247770")
    print(p1)"""