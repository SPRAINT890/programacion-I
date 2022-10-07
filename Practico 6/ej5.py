"""
Queremos modelar una casa con muchas bombillas, de forma que cada bombilla se
puede encender o apagar individualmente.

a. Para ello haremos una clase Bombilla con una variable privada que indique si
está encendida o apagada, así como un método que nos diga si una bombilla
concreta está encendida.

b. Además queremos poner un interruptor general de la luz, tal que si saltan los
fusibles, todas las bombillas quedan apagadas.

c. Cuando el fusible se repara, las bombillas vuelven a estar encendidas o
apagadas, según estuvieran antes del percance.

Para modelar en Python esta característica usaremos una variable que nos diga si
hay luz en el edificio o no.

Cada objeto Bombilla se enciende y se apaga individualmente; pero sólo responde
que está encendida si su interruptor particular está activado y además hay luz
general.

class Bombilla:
 interruptorGeneral ...; // interruptor general
 interruptorParticular ...; // interruptor particular

 def activaGeneral ()
 def desactivaGeneral ()
 def enciende ()
 def apaga ()
 def encendida () 
"""

class Bombilla:
    def __init__(self):
        self._estado = False
    
    #getter
    def get_estado(self):
        return self._estado
    
    #setters
    def set_estado(self, c):
        self._estado = c

if __name__ == '__main__':
    def activarGeneral(obj_list):
        for obj in obj_list:
            obj.set_estado(True)
    
    def desactivarGeneral(obj_list):
        for obj in obj_list:
            obj.set_estado(False)
    
    def enciende()

