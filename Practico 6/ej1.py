"""
Defina una clase que sirva para representar el estado de una bombilla (encendido o
apagado).
a. Defina, asimismo, dos métodos que permitan encender (on) y apagar (off) la
luz de la bombilla.
b. Para probarlo, cree otro método que haga uso de los métodos previamente
definidos y vaya mostrando el estado de la bombilla.
"""
class Bombilla:
    def __init__(self):
        self.estado = False
    
    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

def estado_bombilla(obj):
    print(obj.estado)
    obj.encender()
    print(obj.estado)


if __name__ == "__main__":
    luzA = Bombilla()
    estado_bombilla(luzA)