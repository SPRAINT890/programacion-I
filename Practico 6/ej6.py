"""
Escriba una clase que permita calcular el número PI con una precisión de "n"
decimales. El parámetro "n" deberá introducirse por teclado.
Puede utilizar la siguiente fórmula para aproximar el valor de PI/4:

PI/4 = 1 - 1/3 + 1/5 - 1/7 +... = Suma(n=0,infinito){(-1)^n/(2n+1)}

"""

class Pi:
    def __init__(self, digitos):
        self.numero = self.calcular(digitos)
        
    def __str__(self):
        return str(self.numero)
    
    def calcular(self, digitos):
        n = 10000
        self.numero = 0
        while n > 0:
            self.numero += ((-1)**n)/((2*n)+1)
            n -= 1
        self.numero = round((self.numero+1)*4, int(digitos))
        return self.numero

if __name__ == '__main__':
    pi1 = Pi(10)
    print(pi1)