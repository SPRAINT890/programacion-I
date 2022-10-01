class Auto:
    
    _rueda = 4 #variable de clase
    
    def __init__(self, color, marca, modelo):
        self.color = color #variable de insercion
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = 0
    
    

if __name__ == "__main__":
    auto1 = Auto("Amarillo", "Camaro", "Chevrolet")
    print(auto1.__dict__)