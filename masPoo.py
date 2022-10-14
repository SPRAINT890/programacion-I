class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre
    
    def __str__(self):
        return "Nombre: {}, Edad: {}".format(self.nombre, self.edad)
    
if __name__ == '__main__':
    p1 = Persona("Gaspar", 19)
    p2 = Persona("Gerardo", 30)
    
    if p1 == p2:
        print("son iguales")
    else:
        print("Persona 1: ", p1)
        print("Persona 2: ", p2)