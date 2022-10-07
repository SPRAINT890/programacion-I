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
    def __init__(self, numero):
        self._numero = numero
        self._estado = False
        self._corriente = False
    
    #getter _estado
    def get_estado(self):
        return self._estado
    
    #getter _numero
    def get_numero(self):
        return self._numero
    
    #getter _corriente
    def get_corriente(self):
        return self._corriente
    
    #setter _estado
    def set_estado(self, v):
        self._estado = v
    
    #setter _numero
    def set_numero(self, v):
        self._numero = v
    
    #setter _corriente
    def set_corriente(self, v):
        self._corriente = v

if __name__ == '__main__':
    def activarGeneral(obj_list):
        for obj in obj_list:
            obj.set_corriente(True)
    
    def desactivarGeneral(obj_list):
        for obj in obj_list:
            obj.set_corriente(False)
    
    def enciende(obj):
        obj.set_estado(True)
    
    def apaga(obj):
        obj.set_estado(False)
    
    def encendida(obj):
        corriente = obj.get_corriente()
        prendido = obj.get_estado()
        
        if corriente and not prendido or not corriente:
            return False
        else:
            return True
    
    lista_bombillas = []
    for i in range(10):
        lista_bombillas.append(Bombilla(i))
    
    #prendo la general
    activarGeneral(lista_bombillas)
    
    #prendo las luces
    for bombilla in lista_bombillas:
        enciende(bombilla)
    
    apaga(lista_bombillas[0])
    apaga(lista_bombillas[4])
    apaga(lista_bombillas[9])
    
    #desactivarGeneral(lista_bombillas)
    
    #verifico el estado
    for bombilla in lista_bombillas:
        if encendida(bombilla):
            print("bombilla n° " + str(bombilla.get_numero()) + " esta prendida")
        else:
            print("bombilla n° " + str(bombilla.get_numero()) + " no esta prendida")
