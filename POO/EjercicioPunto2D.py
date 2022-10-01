import math

class Punto2d:
    def __init__(self):
        self._x = 0.0
        self._y = 0.0
    
    @property
    def coord_x(self):
        return self._x
    
    @property
    def coord_y(self):
        return self._y
    
    @coord_x.setter
    def coord_x(self, new_coord_x):
        self.coord_x = new_coord_x
    
    @coord_y.setter
    def coord_y(self, new_coord_y):
        self.coord_y = new_coord_y
    
    def asignar(self, nx, ny):
        self.coord_x = nx
        self.coord_y = ny
    
    def mover(self, incX, incY):
        self.coord_x = self.coord_x + incX
        self.coord_y = self.coord_y + incY
    
    def distancia_origen(self):
        return math.sqrt(self.coord_x**2 + self.coord_y**2)
    
    def distancia_a(self, otroPunto):
        return math.sqrt((self.coord_x - otroPunto)**2 + (self.coord_y - otroPunto)**2)
    
    def __eq__(self, otroPunto):
        return self.coord_x == otroPunto.coord_x and self.coord_y == otroPunto.coord_y
    
    def __str__(self):
        return "Punto2D ({0}, {1})".format(self.coord_x, self.coord_y)
    
    if __name__ == "__main__":
        punto1 = Punto2d()
        print("Punto 1: ", punto1)