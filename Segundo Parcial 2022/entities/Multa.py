class Multa:
    def __init__(self, concepto, importe, esta_paga) -> None:
        self._concepto = concepto
        self._importe = importe
        self._esta_paga = esta_paga
    
    @property
    def concepto(self):
        return self._concepto
    
    @concepto.setter
    def concepto(self, concepto):
        self._concepto = concepto
    
    @property
    def importe(self):
        return self._importe
    
    @importe.setter
    def importe(self, importe):
        self._importe = importe
    
    @property
    def esta_paga(self):
        return self._esta_paga
    
    @esta_paga.setter
    def esta_paga(self, esta_paga):
        self._esta_paga = esta_paga