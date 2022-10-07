"""
Se desea llevar un control del estado de una cuenta corriente; la cuenta corriente
está caracterizada por su saldo y sobre ella se pueden realizar tres tipos de
operaciones:

a. saldo: devuelve el saldo de la cuenta (puede ser negativo).
b. imposición (cantidad): ingresa en la cuenta una cantidad de dinero.
c. reintegro (cantidad): saca de la cuenta una determinada cantidad de dinero.
Suponga que la cuenta inicialmente tiene un saldo de cero.
d. Escriba una clase CuentaCorriente que implemente la funcionalidad descrita;
escriba otro método para probar su funcionamiento

saldo
"""
class CuentaCorriente:
    def __init__(self):
        self.saldo = 0
    
    def estadoDeCuenta(self):
        return self.saldo
    
    def imposicion(self, cantidad):
        self.saldo += cantidad
    
    def reintegro(self, cantidad):
        self.saldo -= cantidad

if __name__ == "__main__":
    gaspar = CuentaCorriente()
    print(gaspar.estadoDeCuenta())
    gaspar.imposicion(100)
    print(gaspar.estadoDeCuenta())
    gaspar.reintegro(2000)
    print(gaspar.estadoDeCuenta())