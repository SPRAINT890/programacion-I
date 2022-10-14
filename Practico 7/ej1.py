"""
Crear una clase que represente a una persona. En ella como datos mínimos se
debe incluir el nombre, su cedula de identidad (sin dígito verificador), su
dirección y teléfono:
a. Crear un constructor para la clase que reciba los atributos de la
persona.
b. Realizar métodos getter y setter para todos los atributos de la clase. 
"""

class Persona:
    def __init__(self, nombre, ci, dir, tel):
        self.nombre = nombre
        self.ci = ci
        self.dir = dir
        self.tel = tel
    
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
    
    @property
    def ci(self):
        return self.ci
    
    @ci.setter
    def ci(self, ci):
        self.ci = ci
    
    @property
    def dir(self):
        return self.dir
    
    @dir.setter
    def ci(self, dir):
        self.dir = dir
    
    @property
    def tel(self):
        return self.tel
    
    @tel.setter
    def tel(self, tel):
        self.tel = tel