"""
Escriba una clase que represente un círculo; el círculo queda perfectamente definido
si se conoce su radio.

a. Defina además, para esta clase, dos métodos que permitan calcular el área
del círculo y el perímetro de la circunferencia que delimita el círculo.

b. Para probar la funcionalidad antes definida, escriba un método que cree un
círculo con un radio dado, y que calcule (y muestre por pantalla) el área y el
perímetro de su circunferencia.
"""
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

if __name__ == "__main__":
    circuloA = Circulo(10)
    print(circuloA.calcular_area())
    print(circuloA.calcular_perimetro())