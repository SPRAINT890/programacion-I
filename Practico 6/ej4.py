"""Se quiere definir una clase que permita controlar un sintonizador digital de emisoras
FM; 
concretamente, lo que se desea es dotar al controlador de una interfaz que
permita subir (up) o bajar (down) la frecuencia (en saltos de 0.5 MHz) y mostrar la
frecuencia sintonizada en un momento dado (display).
Supondremos que el rango de frecuencias a manejar oscila entre los 80 Mhz y los
108 MHz y que al inicio, el controlador sintoniza a 80 MHz.
Si durante una operación de subida o bajada se sobrepasa uno de los dos límites, la
frecuencia sintonizada debe pasar a ser la del extremo contrario.
"""

class ReceptorFM:
    def __init__(self):
        self.minimo = 80.0
        self.maximo = 108.0
        self.sintonizando = 80.0
        self.saltos = 0.5
    
    def display(self):
        return self.sintonizando
    
    def up(self):
        if self.maximo < self.sintonizando + self.saltos:
            self.sintonizando = self.minimo
            pass
        else:
            self.sintonizando += self.saltos

    def down(self):
        if self.minimo > self.sintonizando - self.saltos:
            self.sintonizando = self.maximo
        else:
            self.sintonizando -= self.saltos

if __name__ == "__main__":
    radio = ReceptorFM()
    print(radio.display())
    
    radio.down()
    print(radio.display())
    
    radio.up()
    print(radio.display())
    radio.up()
    print(radio.display())
    radio.up()
    print(radio.display())

