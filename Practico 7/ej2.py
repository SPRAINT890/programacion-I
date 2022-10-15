"""
A los efectos de complementar la clase Persona del ejercicio 1, 

se creará una nueva clase Tarjeta que represente una tarjeta de crédito, las cuales debe
contener las propiedades nombre, número y digito verificador. Agregue a la
clase Persona un atributo mi_tarjeta, que represente una tarjeta de crédito
como también un método set_tarjeta que permita inicializar la tarjeta de la
persona. Por último, cree un método main que cree una Persona de nombre
“John Doe”, cédula “5555555” y esta persona debe poseer una tarjeta “Visa” de
número “777777777777” código de seguridad “456”.
"""
from ej1 import Persona

class Tarjeta_credito:
    def __init__(self, nombre, numero, digito):
        self._nombre = nombre
        self._numero = numero
        self._digito = digito
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def digito(self):
        return self._digito
    
    @digito.setter
    def digito(self, digito):
        self._digito = digito
    
    def __str__(self):
        return "Nombre: {}, Numero: {}, Digitos: {}".format(self.nombre, self.numero, self.digito)

if __name__ == '__main__':
    t1 = Tarjeta_credito("Visa", "777777777777", "456")
    p1 = Persona("John Doe", "5555555", "Gral. Nariño 2388", "91247770", t1)
    print(p1)